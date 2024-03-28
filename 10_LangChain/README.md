# LangChain

[LangChain](https://www.langchain.com/) is an open-source framework designed to simplify the creation of applications that use large language models (LLMs). LangChain has a vibrant community of developers and contributors and is used by many companies and organizations. LangChain utilizes proven Prompt Engineering patterns and techniques to optimize LLMs, ensuring successful and accurate results through verified and tested best practices.

Part of the appeal of LangChain syntax is the capability of breaking down large complex interactions with LLMs into smaller, more manageable steps by composing a reusable [chain](https://python.langchain.com/docs/modules/chains/) process. LangChain provides a syntax for chains([LCEL](https://python.langchain.com/docs/modules/chains/#lcel)), the ability to integrate with external systems through [tools](https://python.langchain.com/docs/integrations/tools/), and end-to-end [agents](https://python.langchain.com/docs/modules/agents/) for common applications.

The concept of an agent is quite similar to that of a chain in LangChain but with one fundamental difference. A chain in LangChain is a hard-coded sequence of steps executed in a specific order. Conversely, an agent leverages the LLM to assess the incoming request with the current context to decide what steps or actions need to be executed and in what order.

LangChain agents can leverage tools and toolkits. A tool can be an integration into an external system, custom code, or even another chain. A toolkit is a collection of tools that can be used to solve a specific problem.

## LangChain RAG pattern

Earlier in this guide, the RAG (Retrieval Augmented Generation) pattern was introduced. In LangChain, the RAG pattern is implemented as part of a chain that combines a retriever and a Large Language Model (generator). The retriever is responsible for finding the most relevant documents for a given query, in this case, doing a vector search on vCore-based Azure Cosmos DB for MongoDB, and the LLM (generator) is responsible for reasoning over the incoming prompt and context.

![LangChain RAG diagram shows the flow of an incoming message through a retriever, augmenting the prompt, parsing the output and returning the final message.](media/langchain_rag.png)

When an incoming message is received, the retriever will vectorize the message and perform a vector search to find the most relevant documents for the given query. The retriever returns a list of documents that are then used to augment the prompt. The augmented prompt is then passed to the LLM (generator) to reason over the prompt and context. The output from the LLM is then parsed and returned as the final message.

> **Note**: A vector store retriever is only one type of retriever that can be used in the RAG pattern. Learn more about retrievers in the [LangChain documentation](https://python.langchain.com/docs/modules/data_connection/retrievers/).

## Lab - Vector search and RAG using LangChain

In this lab uses LangChain to re-implement the RAG pattern introduced in the previous lab. Take note of the readability of the code and how easy it is to compose a reusable RAG chain using LangChain that queries the products vector index in vCore-based Azure Cosmos DB for MongoDB. The lab concludes with the creation of an agent with various tools for the LLM to leverage to fulfill the incoming request.

This lab also requires the data provided in the previous lab titled [Load data into Azure Cosmos DB API for MongoDB collections](../08_Load_Data/README.md#lab---load-data-into-azure-cosmos-db-api-for-mongodb-collections) as well as the populated vector index created in the lab titled [Vector Search using vCore-based Azure Cosmos DB for MongoDB](../09_Vector_Search_Cosmos_DB/README.md#lab---use-vector-search-on-embeddings-in-vcore-based-azure-cosmos-db-for-mongodb). Run all cells in both notebooks to prepare the data for use in this lab.

>**Note**: It is highly recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) for all labs.

Please visit the lab repository to complete [this lab](https://github.com/AzureCosmosDB/Azure-OpenAI-Python-Developer-Guide/blob/main/Labs/lab_4_langchain.ipynb).

Some highlights of the lab include:

### Instantiating a vector store reference

```python
vector_store = AzureCosmosDBVectorSearch.from_connection_string(
    connection_string = CONNECTION_STRING,
    namespace = "cosmic_works.products",
    embedding = embedding_model,
    index_name = "VectorSearchIndex",    
    embedding_key = "contentVector",
    text_key = "_id"
)
```

### Composing a reusable RAG chain

```python
# Create a retriever from the vector store
retriever = vector_store.as_retriever()

# Create the prompt template from the system_prompt text
llm_prompt = PromptTemplate.from_template(system_prompt)

rag_chain = (
    # populate the tokens/placeholders in the llm_prompt 
    # products takes the results of the vector store and formats the documents
    # question is a passthrough that takes the incoming question
    { "products": retriever | format_docs, "question": RunnablePassthrough()}
    | llm_prompt
    # pass the populated prompt to the language model
    | llm
    # return the string ouptut from the language model
    | StrOutputParser()
)
```

### Creating tools for LangChain agents to use

Tools are selected by the Large Language model at runtime. In this case, depending on the incoming user request the LLM will decide which collection in the database to query. The following code shows how to create a tool for the LLM to use to query the products collection in the database.

```python
# create a chain on the retriever to format the documents as JSON
products_retriever_chain = products_retriever | format_docs

tools = [
    Tool(
        name = "vector_search_products", 
        func = products_retriever_chain.invoke,
        description = "Searches Cosmic Works product information for similar products based on the question. Returns the product information in JSON format."
    )
]
```

### Creating tools that call Python functions

Users may query for information that does not have a semantic meaning, such as an ID GUID value or a SKU number. Providing agents with tools to call Python functions to retrieve documents based on these fields is a common practice. The following is an example of adding tools that call out to Python functions for the products collection.

```python
db = pymongo.MongoClient(CONNECTION_STRING).cosmic_works

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

from langchain.tools import StructuredTool

tools.extend([
    StructuredTool.from_function(get_product_by_id),
    StructuredTool.from_function(get_product_by_sku),
    StructuredTool.from_function(get_sales_by_id)
])
```

### Creating an agent armed with tools for vector search and Python functions calling

```python
system_message = SystemMessage(
    content = """
        You are a helpful, fun and friendly sales assistant for Cosmic Works, a bicycle and bicycle accessories store.

        Your name is Cosmo.

        You are designed to answer questions about the products that Cosmic Works sells, the customers that buy them, and the sales orders that are placed by customers.

        If you don't know the answer to a question, respond with "I don't know."
        
        Only answer questions related to Cosmic Works products, customers, and sales orders.
        
        If a question is not related to Cosmic Works products, customers, or sales orders,
        respond with "I only answer questions about Cosmic Works"
    """    
)
agent_executor = create_conversational_retrieval_agent(llm, tools, system_message = system_message, verbose=True)
```
