# Use vector search on embeddings in Azure Cosmos DB for MongoDB vCore

>**NOTE**: Azure Cosmos DB for MongoDB vCore supports vector search on embeddings. This functionality is not supported on RUs-based accounts.

## Embeddings and vector search

Embedding is a way of serializing the semantic meaning of data into a vector representation. Because the generated vector embedding represents the semantic meaning means that when it is searched, it can find similar data based on the semantic meaning of the data, rather than exact text. Data can come from many sources, including text, images, audio, and video. Because the data is represented as a vector, vector search can therefore find similar data across all different types of data.

Embeddings are created by sending data to an embedding model where it is transformed into a vector which then can be stored as a vector field within its source document in Azure Cosmos DB for MongoDB vCore. Azure Cosmos DB for MongoDB vCore supports the creation of vector search indexes on top of these vector fields. A vector search index is a collection of vectors in [latent space](https://idl.cs.washington.edu/papers/latent-space-cartography/) that enables semantic search across all data (vectors) contained within.

![A typical embedding pipeline that demonstrates how source data is transformed into vectors using an embedding model then stored in a document in an Azure Cosmos DB vCore database and exposed via a vector search index.](media/embedding_pipeline.png)

## Why vector search?

Vector search is an important component of the RAG (Retrieval Augmented Generation) pattern. Large Language Model (LLM) data is trained on a snapshot of public data at a point in time. This data does not contain recent public information, nor does it contain private, corporate information. LLMs are also very broad in their knowledge and including information from a RAG process can help it focus accurately on a specific domain.

A vector index search allows for a prompt pre-processing step where information can be semantically retrieved from an index and then used to generate a factually accurate prompt for the LLM to reason over. This provides the knowledge augmentation and focus (attention) to the LLM.

In this example, assume textual data is vectorized and stored within an Azure Cosmos DB for MongoDB vCore database. Both the vectorized data and embeddings/vector field are stored in the same document. A vector search index has been created on the vector field. When a message is received from a chat application, this message is also vectorized using the same embedding model (ex. Azure OpenAI text-embedding-ada-002) which is then used as input to the vector search index. The vector search index returns a list of documents whose vector field is semantically similar to the incoming message. The unvectorized text stored within the same document is then used to augment the LLM prompt. The LLM receives the prompt and generates a response back to the requestor based on the information it has been given.

![A typical vector search request in a RAG scenario depicts an incoming message getting vectorized and used as input to a vector store index search. Multiple results of the vector search are used to build a prompt fed to the LLM. The LLM returns a response back to the requestor.](media/vector_search_flow.png)

## Lab 3 - Use vector search on embeddings in Azure Cosmos DB for MongoDB vCore

In this lab, we'll use a notebook to demonstrate how to add an embedding field to a document, create a vector search index, and perform a vector search query.

Please visit the lab repository to complete this lab.
