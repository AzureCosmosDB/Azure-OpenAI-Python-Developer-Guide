"""
The CosmicWorksAIAgent class encapsulates a LangChain 
agent that can be used to answer questions about Cosmic Works
products, customers, and sales.
"""
import os
import json
from typing import List
import pymongo
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch
from langchain.schema.document import Document
from langchain.agents import Tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.tools import StructuredTool
from langchain_core.messages import SystemMessage

load_dotenv(".env")
DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")
AOAI_ENDPOINT = os.environ.get("AOAI_ENDPOINT")
AOAI_KEY = os.environ.get("AOAI_KEY")
AOAI_API_VERSION = "2023-09-01-preview"
COMPLETIONS_DEPLOYMENT = "completions"
EMBEDDINGS_DEPLOYMENT = "embeddings"
db = pymongo.MongoClient(DB_CONNECTION_STRING).cosmic_works

class CosmicWorksAIAgent:
    """
    The CosmicWorksAIAgent class creates Cosmo, an AI agent
    that can be used to answer questions about Cosmic Works
    products, customers, and sales.
    """
    def __init__(self, session_id: str):
        llm = AzureChatOpenAI(
            temperature = 0,
            openai_api_version = AOAI_API_VERSION,
            azure_endpoint = AOAI_ENDPOINT,
            openai_api_key = AOAI_KEY,
            azure_deployment = COMPLETIONS_DEPLOYMENT
        )
        self.embedding_model = AzureOpenAIEmbeddings(
            openai_api_version = AOAI_API_VERSION,
            azure_endpoint = AOAI_ENDPOINT,
            openai_api_key = AOAI_KEY,
            azure_deployment = EMBEDDINGS_DEPLOYMENT,
            chunk_size=10
        )
        system_message = SystemMessage(
            content = """
                You are a helpful, fun and friendly sales assistant for Cosmic Works, 
                a bicycle and bicycle accessories store.

                Your name is Cosmo.

                You are designed to answer questions about the products that Cosmic Works sells, 
                the customers that buy them, and the sales orders that are placed by customers.

                If you don't know the answer to a question, respond with "I don't know."

                Only answer questions related to Cosmic Works products, customers, and sales orders.
                
                If a question is not related to Cosmic Works products, customers, or sales orders,
                respond with "I only answer questions about Cosmic Works"
            """
        )
        self.agent_executor = create_conversational_retrieval_agent(
                llm,
                self.__create_agent_tools(),
                system_message = system_message,
                memory_key=session_id,
                verbose=True
        )

    def run(self, prompt: str) -> str:
        """
        Run the AI agent.
        """
        result = self.agent_executor({"input": prompt})
        return result["output"]

    def __create_cosmic_works_vector_store_retriever(
            self,
            collection_name: str,
            top_k: int = 3
        ):
        """
        Returns a vector store retriever for the given collection.
        """
        vector_store =  AzureCosmosDBVectorSearch.from_connection_string(
            connection_string = DB_CONNECTION_STRING,
            namespace = f"cosmic_works.{collection_name}",
            embedding = self.embedding_model,
            index_name = "VectorSearchIndex",
            embedding_key = "contentVector",
            text_key = "_id"
        )
        return vector_store.as_retriever(search_kwargs={"k": top_k})

    def __create_agent_tools(self) -> List[Tool]:
        """
        Returns a list of agent tools.
        """
        products_retriever = self.__create_cosmic_works_vector_store_retriever("products")
        customers_retriever = self.__create_cosmic_works_vector_store_retriever("customers")
        sales_retriever = self.__create_cosmic_works_vector_store_retriever("sales")

        # create a chain on the retriever to format the documents as JSON
        products_retriever_chain = products_retriever | format_docs
        customers_retriever_chain = customers_retriever | format_docs
        sales_retriever_chain = sales_retriever | format_docs

        tools = [
            Tool(
                name = "vector_search_products",
                func = products_retriever_chain.invoke,
                description = """
                    Searches Cosmic Works product information for similar products based 
                    on the question. Returns the product information in JSON format.
                    """
            ),
            Tool(
                name = "vector_search_customers",
                func = customers_retriever_chain.invoke,
                description = """
                    Searches Cosmic Works customer information and retrieves similar 
                    customers based on the question. Returns the customer information 
                    in JSON format.
                    """
            ),
            Tool(
                name = "vector_search_sales",
                func = sales_retriever_chain.invoke,
                description = """
                    Searches Cosmic Works customer sales information and retrieves sales order 
                    details based on the question. Returns the sales order information in JSON format.
                    """
            ),
            StructuredTool.from_function(get_product_by_id),
            StructuredTool.from_function(get_product_by_sku),
            StructuredTool.from_function(get_sales_by_id)
        ]
        return tools

def format_docs(docs:List[Document]) -> str:
    """
    Prepares the product list for the system prompt.
    """
    str_docs = []
    for doc in docs:
        # Build the product document without the contentVector
        doc_dict = {"_id": doc.page_content}
        doc_dict.update(doc.metadata)
        if "contentVector" in doc_dict:
            del doc_dict["contentVector"]
        str_docs.append(json.dumps(doc_dict, default=str))
    # Return a single string containing each product JSON representation
    # separated by two newlines
    return "\n\n".join(str_docs)

def get_product_by_id(product_id: str) -> str:
    """
    Retrieves a product by its ID.    
    """
    doc = db.products.find_one({"_id": product_id})
    if "contentVector" in doc:
        del doc["contentVector"]
    return json.dumps(doc)

def get_product_by_sku(sku: str) -> str:
    """
    Retrieves a product by its sku.
    """
    doc = db.products.find_one({"sku": sku})
    if "contentVector" in doc:
        del doc["contentVector"]
    return json.dumps(doc, default=str)

def get_sales_by_id(sales_id: str) -> str:
    """
    Retrieves a sales order by its ID.
    """
    doc = db.sales.find_one({"_id": sales_id})
    if "contentVector" in doc:
        del doc["contentVector"]
    return json.dumps(doc, default=str)
  