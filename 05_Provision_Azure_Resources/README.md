# Provision Azure resources (Azure Cosmos DB workspace, Azure OpenAI, etc.)

TBD once all other modules are complete.

Bicep deployment is available in the `deploy` folder of the lab repository.
Currently deploying the following:
    - Resource Group (this is done manually in the Azure Portal)
    - Azure Cosmos DB API for MongoDB vCore account
    - Azure OpenAI resource
      - Chat GPT-3.5 `completions` model
      - text-embedding-ada-002 model `embeddings` model
    - Azure Container Registry to host Docker images
    - Azure Container Apps Environment to host Docker containers
    - Azure Container App to run Docker containers (initially with hello-world, but updated during the Backend API lab to run the backend Python API)
    - Azure App Service to host Front-End SPA written in React
