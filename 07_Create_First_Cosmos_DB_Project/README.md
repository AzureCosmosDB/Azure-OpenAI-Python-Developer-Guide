# Create your first Cosmos DB project

This section will cover how to create your first Cosmos DB project. We'll use a notebook to demonstrate the basic CRUD operations. We'll also cover using the Azure Cosmos DB Emulator to test code locally.

## Emulator support

Azure Cosmos DB has an emulator that can be used to develop code locally. The emulator supports the API for NoSQL and the API for MongoDB. The use of the emulator does not require an Azure subscription, nor does it incur any costs, so it is ideal for local development and testing. The Azure Cosmos DB emulator can also be utilized with unit tests in a [GitHub Actions CI workflow](https://learn.microsoft.com/azure/cosmos-db/how-to-develop-emulator?tabs=windows%2Cpython&pivots=api-mongodb#use-the-emulator-in-a-github-actions-ci-workflow).

There is not 100% feature parity between the emulator and the cloud service. Visit the [Azure Cosmos DB emulator](https://learn.microsoft.com/azure/cosmos-db/emulator) documentation for more details.

For Windows machines, the emulator can be installed via an installer or by using a Docker container. A Docker image is also available for Linux-based machines.

Learn more about the pre-requisites and installation of the emulator [here](https://learn.microsoft.com/azure/cosmos-db/how-to-develop-emulator?tabs=windows%2Cpython&pivots=api-mongodb).

**The Azure Cosmos DB emulator does not support vector search. To complete the vector search and AI-related labs, a Azure Cosmos DB for NoSQL account in Azure is required.**

## Authentication

Authentication to Azure Cosmos DB API for Mongo DB uses a connection string. The connection string is a URL that contains the authentication information for the Azure Cosmos DB account or local emulator. The username and password used when provisioning the Azure Cosmos DB API for NoSQL service are used in the connection string when authenticating to Azure.

### Retrieving the connection string from the Cosmos DB Emulator

The splash screen or **Quickstart** section of the Cosmos DB Emulator will display the connection string. Access this screen through the following URL: `https://localhost:8081/_explorer/index.html`.

![The Azure Cosmos DB emulator screen displays with the local host url, the Quickstart tab, and the connection string highlighted.](media/emulator_connection_string.png)

### Retrieving the connection string from the Azure portal

Retrieve the connection string from the Azure portal by navigating to the Azure Cosmos DB account and expanding the **Settings** menu item on the left-hand side of the screen. Locate the **Primary Connection String**, and select the icon to make it visible. Copy the connection string and paste it in notepad for future reference.

![The Azure Cosmos DB API for NoSQL Connection strings screen displays with the copy button next to the connection string highlighted.](media/azure_connection_string.png)

## Lab - Create your first Cosmos DB for the NoSQL application

Using a notebook, we'll create a Cosmos DB for the NoSQL application in this lab using the **azure-cosmos** library and the Python language. Both the Azure Cosmos DB Emulator and Azure Cosmos DB account in Azure are supported for completion of this lab.

>**Note**: It is highly recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) for all labs.

Please visit the lab repository to complete [this lab](../Labs/lab_1_first_application.ipynb).

The following concepts are covered in detail in this lab:

### Creating a database client

The `azure-cosmos` library is used to create a Cosmos DB API for NoSQL database client. The client enables both DDL (data definition language) and DML (data manipulation language) operations.

```python
client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )
```

### Creating a database

The `create_database` method is used to create a database. If the database already exists, an exception is thrown, therefore verify the database already exists before creating it.

```python
client.create_database(id=id)
```

### Creating a container

In progress

### Creating a document

In progress

### Reading a document

In progress

### Updating a document

In progress

### Deleting a document

In progress

### Querying documents

In progress
