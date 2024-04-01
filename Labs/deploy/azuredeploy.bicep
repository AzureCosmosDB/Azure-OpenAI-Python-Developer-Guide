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
Unique name for the deployed services below. Max length 17 characters, alphanumeric only:
- Azure Cosmos DB for MongoDB vCore
- Azure OpenAI Service

The name defaults to a unique string generated from the resource group identifier. Prefixed with
**dg** 'developer guide' as the id may start with a number which is an invalid name for
many resources.
''')
@maxLength(17)
param name string = 'dg${uniqueString(resourceGroup().id)}'

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

@description('Azure Container Registry SKU. Defaults to **Basic**')
param acrSku string = 'Basic'

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
    sku: {
      name: 'Standard'
      capacity: 120
    }
  }
  embeddingsModel: {
    name: 'text-embedding-ada-002'
    version: '2'
    deployment: {
      name: 'embeddings'
    }
    sku: {
      name: 'Standard'
      capacity: 120     
    }
  }
}

var mongovCoreSettings = {
  mongoClusterName: '${name}-mongo'
  mongoClusterLogin: mongoDbUserName
  mongoClusterPassword: mongoDbPassword
}

var appServiceSettings = {
  plan: {
    name: '${name}-web'
    sku: appServiceSku
  }
  web: {
    name: '${name}-web'
    git: {
      repo: 'https://github.com/AzureCosmosDB/Azure-OpenAI-Developer-Guide-Front-End.git'
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

resource openAiAccount 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
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

resource openAiEmbeddingsModelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: openAiSettings.embeddingsModel.deployment.name  
  sku: {
    name: openAiSettings.embeddingsModel.sku.name
    capacity: openAiSettings.embeddingsModel.sku.capacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: openAiSettings.embeddingsModel.name
      version: openAiSettings.embeddingsModel.version
    }
  }
}

resource openAiCompletionsModelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: openAiSettings.completionsModel.deployment.name
  dependsOn: [
    openAiEmbeddingsModelDeployment
  ]
  sku: {
    name: openAiSettings.completionsModel.sku.name
    capacity: openAiSettings.completionsModel.sku.capacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: openAiSettings.completionsModel.name
      version: openAiSettings.completionsModel.version
    }    
  }
}

/* *************************************************************** */
/* Logging and instrumentation */
/* *************************************************************** */

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2021-06-01' = {
  name: '${name}-loganalytics'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
  }
}
resource appServiceWebInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: '${appServiceSettings.web.name}-appi'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
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
    API_ENDPOINT: 'https://${backendApiContainerApp.properties.configuration.ingress.fqdn}'
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
}


/* *************************************************************** */
/* Registry for Back-end API Image - Azure Container Registry */
/* *************************************************************** */
resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: replace('${name}registry','-', '')
  location: location
  sku: {
    name: acrSku
  }
  properties: {
    adminUserEnabled: true
  }
}

/* *************************************************************** */
/* Container environment - Azure Container App Environment  */
/* *************************************************************** */
resource containerAppEnvironment 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: '${name}-containerappenv'
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
    workloadProfiles: [
      {
        name: 'Warm'
        minimumCount: 1
        maximumCount: 10
        workloadProfileType: 'E4'
      }
    ]
    infrastructureResourceGroup: 'ME_${resourceGroup().name}'
  }
}

/* *************************************************************** */
/* Back-end API App Application - Azure Container App */
/* deploys default hello world */
/* *************************************************************** */
resource backendApiContainerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: '${name}-api'
  location: location
  properties: {
    environmentId: containerAppEnvironment.id
    configuration: {
      ingress: {
        external: true
        targetPort: 80
        allowInsecure: false
        traffic: [
          {
            latestRevision: true
            weight: 100
          }
        ]   
        corsPolicy: {
          allowCredentials: false
          allowedHeaders: [
            '*'
          ]
          allowedOrigins: [
            '*'
          ]
        }
      }
      registries: [
        {
          server: containerRegistry.name
          username: containerRegistry.properties.loginServer
          passwordSecretRef: 'container-registry-password'
        }
      ]
      secrets: [
        {
          name: 'container-registry-password'
          value: containerRegistry.listCredentials().passwords[0].value
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'hello-world'
          image: 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
          resources: {
            cpu: 1
            memory: '2Gi'
          }         
        }
      ]
      scale: {
        minReplicas: 1
        maxReplicas: 1
      }
    }
  }
}
