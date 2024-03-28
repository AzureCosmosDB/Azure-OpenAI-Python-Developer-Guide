# Lab - Backend API

In the previous lab, a LangChain agent was created armed with tools to do vector lookups and concrete document id lookups via function calling. In this lab, the agent functionality needs to be extracted into a backend api for the frontend application that will allow users to interact with the agent.

This lab implements a backend API using FastAPI that exposes the LangChain agent functionality. The provided code leverages Docker containers and includes full step-by-step instructions to run and test the API locally as well as deployed to [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) (leveraging the [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)).

This lab also requires the data provided in the previous lab titled [Load data into Azure Cosmos DB API for MongoDB collections](../08_Load_Data/README.md#lab---load-data-into-azure-cosmos-db-api-for-mongodb-collections) as well as the populated vector index created in the lab titled [Vector Search using vCore-based Azure Cosmos DB for MongoDB](../09_Vector_Search_Cosmos_DB/README.md#lab---use-vector-search-on-embeddings-in-vcore-based-azure-cosmos-db-for-mongodb). Run all cells in both notebooks to prepare the data for use in this lab.

>**Note**: It is highly recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) for all labs.

Please visit the lab repository to complete [this lab](https://github.com/AzureCosmosDB/Azure-OpenAI-Python-Developer-Guide/blob/main/Labs/lab_4_langchain.ipynb).
