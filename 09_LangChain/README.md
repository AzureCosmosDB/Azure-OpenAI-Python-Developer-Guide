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

## Lab 4 - Vector search and RAG using LangChain

In this lab, you will learn to use LangChain to re-implement the RAG pattern introduced in Lab 3. Take note of the readability of the code and how easy it is to compose a reusable RAG chain using LangChain that queries the products vector index in vCore-based Azure Cosmos DB for MongoDB. Lab 4 concludes with the creation of an agent with various tools for the LLM to leverage to fulfill the incoming request.
