/* *************************************************************** 
Azure Cosmos DB + Azure OpenAI Python developer guide lab
******************************************************************
This Azure resource deployment template uses some of the following practices:
- [Abbrevation examples for Azure resources](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations)
*/



/* *************************************************************** */
/* Parameters */
/* *************************************************************** */

@description('Location where all resources will be deployed. This value defaults to the **East US** region.')
@allowed([  
  'eastus'  
  'francecentral'
  'southcentralus'
  'uksouth'
  'westeurope'
])
param location string = 'eastus'

@description('''
Unique name for the deployed services below. Max length 15 characters, alphanumeric only:
- Azure Cosmos DB for MongoDB vCore
- Azure OpenAI Service

The name defaults to a unique string generated from the resource group identifier.
''')
@maxLength(15)
param name string = uniqueString(resourceGroup().id)

@description('Specifies the SKU for the Azure App Service plan. Defaults to **B1**')
@allowed([
  'B1'
  'S1'
  'P0v3'
])
param appServiceSku string = 'P0v3' //'B1'

@description('Specifies the SKU for the Azure OpenAI resource. Defaults to **S0**')
@allowed([
  'S0'
])
param openAiSku string = 'S0'

@description('MongoDB vCore user Name. No dashes.')
param mongoDbUserName string

@description('MongoDB vCore password. 8-256 characters, 3 of the following: lower case, upper case, numeric, symbol.')
@minLength(8)
@maxLength(256)
@secure()
param mongoDbPassword string



/*
@description('Git repository URL for the application source. This defaults to the [`solliancenet/cosmos-db-openai-python-dev-guide-labs`](https://github.com/solliancenet/cosmos-db-openai-python-dev-guide-labs.git) repository.')
param appGitRepository string = 'https://github.com/solliancenet/cosmos-db-openai-python-dev-guide-labs.git'

@description('Git repository branch for the application source. This defaults to the [**main** branch of the `solliancenet/cosmos-db-openai-python-dev-guide-labs`](https://github.com/solliancenet/cosmos-db-openai-python-dev-guide-labs/tree/main) repository.')
param appGetRepositoryBranch string = 'main'
*/

/* *************************************************************** */
/* Variables */
/* *************************************************************** */

var openAiSettings = {
  name: '${name}-openai'
  sku: openAiSku
  maxConversationTokens: '100'
  maxCompletionTokens: '500'
  completionsModel: {
    name: 'gpt-35-turbo'
    version: '0613'
    deployment: {
      name: 'completions'
    }
  }
  embeddingsModel: {
    name: 'text-embedding-ada-002'
    version: '2'
    deployment: {
      name: 'embeddings'
    }
  }
}

var mongovCoreSettings = {
  mongoClusterName: '${name}-mongo'
  mongoClusterLogin: mongoDbUserName
  mongoClusterPassword: mongoDbPassword

  mongoDatabaseName: 'cosmic_works'
  mongoCollectionNames: 'products,customers,sales'
}

var appServiceSettings = {
  plan: {
    name: '${name}-web'
    sku: appServiceSku
  }
  web: {
    name: '${name}-web'
    git: {
      repo: 'https://github.com/crpietschmann/cosmos-db-dev-guide-frontend-app.git'
      branch: 'main'
    }
  }
  api: {
    name: '${name}-api'
    git: {
      repo: 'https://github.com/crpietschmann/cosmos-db-dev-guide-backend-app-python.git'
      branch: 'main'
    }
  }
}



/* *************************************************************** */
/* Azure Cosmos DB for MongoDB vCore */
/* *************************************************************** */

resource mongoCluster 'Microsoft.DocumentDB/mongoClusters@2023-03-01-preview' = {
  name: mongovCoreSettings.mongoClusterName
  location: location
  properties: {
    administratorLogin: mongovCoreSettings.mongoClusterLogin
    administratorLoginPassword: mongovCoreSettings.mongoClusterPassword
    serverVersion: '5.0'
    nodeGroupSpecs: [
      {
        kind: 'Shard'
        sku: 'M30'
        diskSizeGB: 128
        enableHa: false
        nodeCount: 1
      }
    ]
  }
}

resource mongoFirewallRulesAllowAzure 'Microsoft.DocumentDB/mongoClusters/firewallRules@2023-03-01-preview' = {
  parent: mongoCluster
  name: 'allowAzure'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '0.0.0.0'
  }
}

resource mongoFirewallRulesAllowAll 'Microsoft.DocumentDB/mongoClusters/firewallRules@2023-03-01-preview' = {
  parent: mongoCluster
  name: 'allowAll'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '255.255.255.255'
  }
}


/* *************************************************************** */
/* Azure OpenAI */
/* *************************************************************** */

resource openAiAccount 'Microsoft.CognitiveServices/accounts@2022-12-01' = {
  name: openAiSettings.name
  location: location
  sku: {
    name: openAiSettings.sku
  }
  kind: 'OpenAI'
  properties: {
    customSubDomainName: openAiSettings.name
    publicNetworkAccess: 'Enabled'
  }
}

resource openAiEmbeddingsModelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2022-12-01' = {
  parent: openAiAccount
  name: openAiSettings.embeddingsModel.deployment.name
  properties: {
    model: {
      format: 'OpenAI'
      name: openAiSettings.embeddingsModel.name
      version: openAiSettings.embeddingsModel.version
    }
    scaleSettings: {
      scaleType: 'Standard'
    }
  }
}

resource openAiCompletionsModelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2022-12-01' = {
  parent: openAiAccount
  name: openAiSettings.completionsModel.deployment.name
  properties: {
    model: {
      format: 'OpenAI'
      name: openAiSettings.completionsModel.name
      version: openAiSettings.completionsModel.version
    }
    scaleSettings: {
      scaleType: 'Standard'
    }
  }
  dependsOn: [
    openAiEmbeddingsModelDeployment
  ]
}



/* *************************************************************** */
/* App Plan Hosting - Azure App Service Plan */
/* *************************************************************** */

resource appServicePlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: '${appServiceSettings.plan.name}-asp'
  location: location
  sku: {
    name: appServiceSettings.plan.sku
  }
  kind: 'linux'
  properties: {
    reserved: true
  }
}


/* *************************************************************** */
/* Front-end Web App Hosting - Azure App Service */
/* *************************************************************** */

resource appServiceWeb 'Microsoft.Web/sites@2022-03-01' = {
  name: appServiceSettings.web.name
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'NODE|20-lts'
      appCommandLine: 'pm2 serve /home/site/wwwroot/dist --no-daemon --spa'
      alwaysOn: true
    }
  }
}

resource appServiceWebSettings 'Microsoft.Web/sites/config@2022-03-01' = {
  parent: appServiceWeb
  name: 'appsettings'
  kind: 'string'
  properties: {
    APPINSIGHTS_INSTRUMENTATIONKEY: appServiceWebInsights.properties.InstrumentationKey
    API_ENDPOINT: 'https://${appServiceApi.properties.defaultHostName}'
  }
}

resource appServiceWebConnectionStrings 'Microsoft.Web/sites/config@2022-03-01' = {
  parent: appServiceWeb
  name: 'connectionstrings'
  kind: 'string'
  properties: {
    MONGODB__CONNECTION: {
      value: 'mongodb+srv://${mongovCoreSettings.mongoClusterLogin}:${mongovCoreSettings.mongoClusterPassword}@${mongovCoreSettings.mongoClusterName}.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
      type: 'Custom'
    }
  }
}

resource appServiceWebInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: '${appServiceSettings.web.name}-appi'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
  }
}

resource appServiceWebDeployment 'Microsoft.Web/sites/sourcecontrols@2021-03-01' = {
  parent: appServiceWeb
  name: 'web'
  properties: {
    repoUrl: appServiceSettings.web.git.repo
    branch: appServiceSettings.web.git.branch
    isManualIntegration: true
  }
  dependsOn: [
    appServiceWebSettings
  ]
}


/* *************************************************************** */
/* Back-end API Hosting - Azure App Service */
/* *************************************************************** */

resource appServiceApi 'Microsoft.Web/sites@2022-03-01' = {
  name: appServiceSettings.api.name
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.12'
      alwaysOn: true
      httpLoggingEnabled: true
      appCommandLine: 'uvicorn --host "0.0.0.0" --port 443 app:app --reload'
    }
  }
}

resource appServiceApiSettings 'Microsoft.Web/sites/config@2022-03-01' = {
  parent: appServiceApi
  name: 'appsettings'
  kind: 'string'
  properties: {
    ENABLE_ORYX_BUILD: 'true'
    SCM_DO_BUILD_DURING_DEPLOYMENT: 'true'
    WEBSITE_ENABLE_DEFAULT_CODE_PROFILER: 'true'
    APPINSIGHTS_INSTRUMENTATIONKEY: appServiceWebInsights.properties.InstrumentationKey
    APPINSIGHTS_PROFILERFEATURE_VERSION: '1.0.0'
    DiagnosticServices_EXTENSION_VERSION: '~3'
    WEBSITE_HTTPLOGGING_RETENTION_DAYS: '7'
    OPENAI__ENDPOINT: openAiAccount.properties.endpoint
    OPENAI__KEY: openAiAccount.listKeys().key1
    OPENAI__EMBEDDINGSDEPLOYMENT: openAiEmbeddingsModelDeployment.name
    OPENAI__MAXTOKENS: '8191'
    MONGODB__DATABASENAME: mongovCoreSettings.mongoDatabaseName
    MONGODB__COLLECTIONNAMES: mongovCoreSettings.mongoCollectionNames
  }
}

resource appServiceApiConnectionStrings 'Microsoft.Web/sites/config@2022-03-01' = {
  parent: appServiceApi
  name: 'connectionstrings'
  kind: 'string'
  properties: {
    MONGODB__CONNECTION: {
      value: 'mongodb+srv://${mongovCoreSettings.mongoClusterLogin}:${mongovCoreSettings.mongoClusterPassword}@${mongovCoreSettings.mongoClusterName}.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
      type: 'Custom'
    }
  }
}

resource appServiceApiDeployment 'Microsoft.Web/sites/sourcecontrols@2021-03-01' = {
  parent: appServiceApi
  name: 'web'
  properties: {
    repoUrl: appServiceSettings.api.git.repo
    branch: appServiceSettings.api.git.branch
    isManualIntegration: true
  }
  dependsOn: [
    appServiceApiSettings
  ]
}


/* *************************************************************** */
/* Outputs */
/* *************************************************************** */

output deployedWebUrl string = appServiceWeb.properties.defaultHostName

output deployedApiUrl string = appServiceApi.properties.defaultHostName
