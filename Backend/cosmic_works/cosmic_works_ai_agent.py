"""
Class: CosmicWorksAIAgent
Description: 
    The CosmicWorksAIAgent class creates Cosmo, an AI agent
    that can be used to answer questions about Cosmic Works
    products, customers, and sales.
"""
import os
import json
from pydantic import BaseModel
from typing import Type, TypeVar
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from azure.cosmos import CosmosClient, ContainerProxy
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import StructuredTool
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from models import Product, SalesOrder
from retrievers import AzureCosmosDBNoSQLRetriever

from chat_session_state.cosmosdb_chat_session_state_provider import CosmosDBChatSessionStateProvider

T = TypeVar('T', bound=BaseModel)

# Load settings for the notebook
load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_DB_CONNECTION_STRING")
EMBEDDINGS_DEPLOYMENT_NAME = "embeddings"
COMPLETIONS_DEPLOYMENT_NAME = "completions"
AOAI_ENDPOINT = os.environ.get("AOAI_ENDPOINT")
AOAI_KEY = os.environ.get("AOAI_KEY")
AOAI_API_VERSION = "2024-06-01"

# Initialize the Azure Cosmos DB client, database and product (with vector) container
client = CosmosClient.from_connection_string(CONNECTION_STRING)
db = client.get_database_client("cosmic_works")
product_v_container = db.get_container_client("product_v")
sales_order_container = db.get_container_client("salesOrder")

# Create an instance of the CosmosDBChatSessionStateProvider class
# This will be used to load or create Chat Sessions
chat_session_state_provider = CosmosDBChatSessionStateProvider()


class CosmicWorksAIAgent:
    """
    The CosmicWorksAIAgent class creates Cosmo, an AI agent
    that can be used to answer questions about Cosmic Works
    products, customers, and sales.
    """
    def __init__(self, session_id: str):
        self.session_id = session_id

        self.chat_session = chat_session_state_provider.load_or_create_chat_session(session_id)

        llm = AzureChatOpenAI(
            temperature = 0,
            openai_api_version = AOAI_API_VERSION,
            azure_endpoint = AOAI_ENDPOINT,
            openai_api_key = AOAI_KEY,
            azure_deployment = COMPLETIONS_DEPLOYMENT_NAME
        )
        embedding_model = AzureOpenAIEmbeddings(
            openai_api_version = AOAI_API_VERSION,
            azure_endpoint = AOAI_ENDPOINT,
            openai_api_key = AOAI_KEY,
            azure_deployment = EMBEDDINGS_DEPLOYMENT_NAME,
            chunk_size=800
        )
        agent_instructions = """           
                You are a helpful, fun and friendly sales assistant for Cosmic Works, a bicycle and bicycle accessories store.
                Your name is Cosmo.
                You are designed to answer questions about the products that Cosmic Works sells, the customers that buy them, and the sales orders that are placed by customers.
                If you don't know the answer to a question, respond with "I don't know."      
                Only answer questions related to Cosmic Works products, customers, and sales orders.
                If a question is not related to Cosmic Works products, customers, or sales orders,
                respond with "I only answer questions about Cosmic Works"
            """
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", agent_instructions),
                MessagesPlaceholder("chat_history", optional=True),
                ("human", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )
        products_retriever = AzureCosmosDBNoSQLRetriever(
            embedding_model = embedding_model,
            container = product_v_container,
            model = Product,
            vector_field_name = "contentVector",
            num_results = 5   
        )
        tools = [create_retriever_tool(
                    retriever = products_retriever,
                    name = "vector_search_products",
                    description = "Searches Cosmic Works product information for similar products based on the question. Returns the product information in JSON format."
                ),
                StructuredTool.from_function(get_product_by_id),
                StructuredTool.from_function(get_product_by_sku),
                StructuredTool.from_function(get_sales_by_id)]
        agent = create_openai_functions_agent(llm, tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)
    
    def run(self, prompt: str) -> str:
        """
        Run the AI agent.
        """

        # Add the existing chat history to the prompt
        chat_history = [{"role": msg["role"], "content": msg["content"]} for msg in self.chat_session.history]
        full_prompt = {
            "input": prompt,
            "chat_history": chat_history
        }

        # Run the AI agent with the chat history context
        result = self.agent_executor.invoke(full_prompt)
        response = result["output"]

        # Update session chat history with new interaction
        self.chat_session.history.append({"role": "user", "content": prompt})
        self.chat_session.history.append({"role": "assistant", "content": response})

        # Save updated session chat history to Cosmos DB
        chat_session_state_provider.upsert_session(self.chat_session)

        return response
        
# Tools helper methods
def delete_attribute_by_alias(instance: BaseModel, alias:str):
    """
    Removes an attribute from a Pydantic model instance by its alias.
    """
    for model_field in instance.model_fields:
        field = instance.model_fields[model_field]            
        if field.alias == alias:
            delattr(instance, model_field)
            return

def get_single_item_by_field_name(
        container:ContainerProxy,
        field_name:str,
        field_value:str,
        model:Type[T]) -> T:
    """
    Retrieves a single item from the Azure Cosmos DB NoSQL database by a specific field and value.
    """
    query = f"SELECT TOP 1 * FROM itm WHERE itm.{field_name} = @value"
    parameters = [
        {
            "name": "@value", 
            "value": field_value
        }
    ]
    items = list(container.query_items(
        query=query,
        parameters=parameters,
        enable_cross_partition_query=True
    ))
    
    # Check if any item is returned
    if not items:
        return None  # Return None if no item is found

    # Cast the item to the provided model
    item_casted = model(**items[0])
    return item_casted
    # item = list(container.query_items(
    #     query=query,
    #     parameters=parameters,
    #     enable_cross_partition_query=True
    # ))[0]
    # item_casted = model(**item)    
    # return item_casted

def get_product_by_id(product_id: str) -> str:
    """
    Retrieves a product by its ID.    
    """
    item = get_single_item_by_field_name(product_v_container, "id", product_id, Product)
    if item is None:
        return json.dumps({"error": "Product with 'id' ({id}) not found."}, indent=4)
    delete_attribute_by_alias(item, "contentVector")
    return json.dumps(item, indent=4, default=str)    

def get_product_by_sku(sku: str) -> str:
    """
    Retrieves a product by its sku.
    """
    item = get_single_item_by_field_name(product_v_container, "sku", sku, Product)
    if item is None:
        return json.dumps({"error": "Product with 'sku' ({sku}) not found."}, indent=4)
    delete_attribute_by_alias(item, "contentVector")
    return json.dumps(item, indent=4, default=str)
    
def get_sales_by_id(sales_id: str) -> str:
    """
    Retrieves a sales order by its ID.
    """
    item = get_single_item_by_field_name(sales_order_container, "id", sales_id, SalesOrder)
    if item is None:
        return json.dumps({"error": "SalesOrder with 'id' ({id}) not found."}, indent=4)
    return json.dumps(item, indent=4, default=str)
