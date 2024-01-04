# Provision Azure resources (Azure Cosmos DB workspace, Azure OpenAI, etc.)

TBD once all other modules are complete.

Bicep deployment is available in the `deploy` folder of the lab repository.
Currently deploying the following:
    - Resource Group
    - Azure Cosmos DB API for MongoDB vCore account
    - Azure OpenAI resource
      - Chat GPT-3.5 `completions` model
      - text-embedding-ada-002 model `embeddings` model
    - Azure App Service to host Front-End SPA written in React
    - Azure App Service to host Back-end API written in Python
