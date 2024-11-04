# LangChain

[LangChain](https://www.langchain.com/) is an open-source framework designed to simplify the creation of applications that use large language models (LLMs). LangChain has a vibrant community of developers and contributors and is used by many companies and organizations. LangChain utilizes proven Prompt Engineering patterns and techniques to optimize LLMs, ensuring successful and accurate results through verified and tested best practices.

Part of the appeal of LangChain syntax is the capability of breaking down large complex interactions with LLMs into smaller, more manageable steps by composing a reusable chain process. LangChain provides a syntax for chains([LCEL](https://python.langchain.com/docs/concepts/#langchain-expression-language-lcel)), the ability to integrate with external systems through [tools](https://python.langchain.com/docs/concepts/#tools), and end-to-end [agents](https://python.langchain.com/docs/concepts/#agents) for common applications.

The concept of an agent is quite similar to that of a chain in LangChain but with one fundamental difference. A chain in LangChain is a hard-coded sequence of steps executed in a specific order. Conversely, an agent leverages the LLM to assess the incoming request with the current context to decide what steps or actions need to be executed and in what order.

LangChain agents can leverage tools and toolkits. A tool can be an integration into an external system, custom code, a retriever, or even another chain. A toolkit is a collection of tools that can be used to solve a specific problem.

## LangChain RAG pattern

Earlier in this guide, the RAG (Retrieval Augmented Generation) pattern was introduced. In LangChain, the RAG pattern is implemented as part of a chain that combines a retriever and a Large Language Model (generator). The retriever is responsible for finding the most relevant documents for a given query, in this case, doing a vector search on Azure Cosmos DB for NoSQL, and the LLM (generator) is responsible for reasoning over the incoming prompt and context.

![LangChain RAG diagram shows the flow of an incoming message through a retriever, augmenting the prompt, parsing the output and returning the final message.](media/langchain_rag.png)

When an incoming message is received, the retriever will vectorize the message and perform a vector search to find the most relevant documents for the given query. The retriever returns a list of documents that are then used to augment the prompt. The augmented prompt is then passed to the LLM (generator) to reason over the prompt and context. The output from the LLM is then parsed and returned as the final message.

> **Note**: A vector store retriever is only one type of retriever that can be used in the RAG pattern. Learn more about retrievers in the [LangChain documentation](https://python.langchain.com/docs/concepts/#retrievers).

## Lab - Vector search and RAG using LangChain

In this lab uses LangChain to re-implement the RAG pattern introduced in the previous lab. Take note of the readability of the code and how easy it is to compose a reusable RAG chain using LangChain that queries the products vector index in Azure Cosmos DB for NoSQL. The lab concludes with the creation of an agent with various tools for the LLM to leverage to fulfill the incoming request.

This lab also requires the data provided in the previous lab titled [Load data into Azure Cosmos DB for NoSQL containers](../08_Load_Data/README.md#lab---load-data-into-azure-cosmos-db-api-for-nosql-containers) as well as the populated vector index created in the lab titled [Vector Search using Azure Cosmos DB for NoSQL](../09_Vector_Search_Cosmos_DB/README.md#lab---use-vector-search-on-embeddings-in-azure-cosmos-db-for-nosql). Run all cells in both notebooks to prepare the data for use in this lab.

>**Note**: It is highly recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) for all labs.

Please visit the lab repository to complete [this lab](../Labs/lab_4_langchain.ipynb).

Some highlights of the lab include:

### Creating a custom LangChain retriever for Azure Cosmos DB for NoSQL

```python
class AzureCosmosDBNoSQLRetriever(BaseRetriever):
    """
    A custom LangChain retriever that uses Azure Cosmos DB NoSQL database for vector search.
    """
    embedding_model: AzureOpenAIEmbeddings
    container: ContainerProxy
    model: Type[T]
    vector_field_name: str
    num_results: int=5

    def __get_embeddings(self, text: str) -> List[float]:       
        """
        Returns embeddings vector for a given text.
        """
        embedding = embedding_model.embed_query(text)        
        time.sleep(0.5) # rest period to avoid rate limiting on AOAI
        return embedding
    
    def __get_item_by_id(self, id) -> T:
        """
        Retrieves a single item from the Azure Cosmos DB NoSQL database by its ID.
        """
        query = "SELECT * FROM itm WHERE itm.id = @id"
        parameters = [
            {"name": "@id", "value": id}
        ]    
        item = list(self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))[0]
        return self.model(**item)
    
    def __delete_attribute_by_alias(self, instance: BaseModel, alias):
        for model_field in instance.model_fields:
            field = instance.model_fields[model_field]            
            if field.alias == alias:
                delattr(instance, model_field)
                return
    
    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """
        Performs a synchronous vector search on the Azure Cosmos DB NoSQL database.
        """
        embedding = self.__get_embeddings(query)
        items = self.container.query_items(
            query=f"""SELECT TOP @num_results itm.id, VectorDistance(itm.{self.vector_field_name}, @embedding) AS SimilarityScore 
                    FROM itm
                    ORDER BY VectorDistance(itm.{self.vector_field_name}, @embedding)
                    """,
            parameters = [
                { "name": "@num_results", "value": self.num_results },
                { "name": "@embedding", "value": embedding }            
            ],
            enable_cross_partition_query=True
        ) 
        returned_docs = []
        for item in items:
            itm = self.__get_item_by_id(item["id"])  
            # Remove the vector field from the returned item so it doesn't fill the context window
            self.__delete_attribute_by_alias(itm, self.vector_field_name)            
            returned_docs.append(Document(page_content=json.dumps(itm, indent=4, default=str), metadata={"similarity_score": item["SimilarityScore"]}))
        return returned_docs
    
    async def _aget_relevant_documents(
        self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun
    ) -> List[Document]:
        """
        Performs an asynchronous vector search on the Azure Cosmos DB NoSQL database.        
        """
        raise Exception(f"Asynchronous search not implemented.")
```

### Composing a reusable RAG chain

```python
# Create an instance of the AzureCosmosDBNoSQLRetriever
products_retriever = AzureCosmosDBNoSQLRetriever(
    embedding_model = embedding_model,
    container = product_v_container,
    model = Product,
    vector_field_name = "contentVector",
    num_results = 5   
)

# Create the prompt template from the system_prompt text
llm_prompt = PromptTemplate.from_template(system_prompt)

rag_chain = (
    # populate the tokens/placeholders in the llm_prompt    
    # question is a passthrough that takes the incoming question
    { "products": products_retriever, "question": RunnablePassthrough()}
    | llm_prompt
    # pass the populated prompt to the language model
    | llm
    # return the string ouptut from the language model
    | StrOutputParser()
)
```

### Creating tools for LangChain agents to use

Tools are selected by the Large Language model at runtime. In this case, depending on the incoming user request the LLM will decide which container in the database to query. The following code shows how to create a tool for the LLM to use to query the products collection in the database.

```python
# Create a tool that will use the product vector search in Azure Cosmos DB for NoSQL
products_retriever_tool = create_retriever_tool(
    retriever = products_retriever,
    name = "vector_search_products",
    description = "Searches Cosmic Works product information for similar products based on the question. Returns the product information in JSON format."
)
tools = [products_retriever_tool]
```

### Creating tools that call Python functions

Users may query for information that does not have a semantic meaning, such as an ID GUID value or a SKU number. Providing agents with tools to call Python functions to retrieve documents based on these fields is a common practice. The following is an example of adding tools that call out to Python functions for the products collection.

```python
def get_product_by_id(product_id: str) -> str:
    """
    Retrieves a product by its ID.    
    """
    item = get_single_item_by_field_name(product_v_container, "id", product_id, Product)
    delete_attribute_by_alias(item, "contentVector")
    return json.dumps(item, indent=4, default=str)    

def get_product_by_sku(sku: str) -> str:
    """
    Retrieves a product by its sku.
    """
    item = get_single_item_by_field_name(product_v_container, "sku", sku, Product)
    delete_attribute_by_alias(item, "contentVector")
    return json.dumps(item, indent=4, default=str)
    
def get_sales_by_id(sales_id: str) -> str:
    """
    Retrieves a sales order by its ID.
    """
    item = get_single_item_by_field_name(sales_order_container, "id", sales_id, SalesOrder)
    return json.dumps(item, indent=4, default=str)

tools.extend([
    StructuredTool.from_function(get_product_by_id),
    StructuredTool.from_function(get_product_by_sku),
    StructuredTool.from_function(get_sales_by_id)
])
```

### Creating an agent armed with tools for vector search and Python functions calling

```python
agent_instructions = """           
        Your name is "Willie". You are an AI assistant for the Cosmic Works bike store. You help people find production information for bikes and accessories. Your demeanor is friendly, playful with lots of energy.
        Do not include citations or citation numbers in your responses. Do not include emojis.
        You are designed to answer questions about the products that Cosmic Works sells, the customers that buy them, and the sales orders that are placed by customers.
        If you don't know the answer to a question, respond with "I don't know."      
        Only answer questions related to Cosmic Works products, customers, and sales orders.
        If a question is not related to Cosmic Works products, customers, or sales orders,
        respond with "I only answer questions about Cosmic Works"
    """  

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", agent_instructions),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)  
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)
```
