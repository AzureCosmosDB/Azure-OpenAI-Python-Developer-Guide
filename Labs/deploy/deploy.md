# Solution deployment

## Prerequisites

- Owner on Azure subscription
- Account approved for Azure OpenAI service
- Azure CLI installed
- Azure PowerShell installed

## Clone the repository

Create a folder to house the repository. Open a terminal and navigate to the folder. Clone the repository, then navigate to the `Labs/deploy` folder within the repository.

```bash
git clone https://github.com/solliancenet/Cosmos-DB-NoSQL-OpenAI-Python-Dev-Guide.git

cd Cosmos-DB-NoSQL-OpenAI-Python-Dev-Guide
cd Labs
cd deploy
```

Open the `azuredeploy.parameters.json` file, and inspect the values, modify as deemed appropriate.

## Login to Azure

Open a terminal window and log in to Azure using the following command:

```Powershell
Connect-AzAccount
```

### Set the desired subscription (Optional)

If you have more than one subscription associated with your account, set the desired subscription using the following command:

```Powershell
Set-AzContext -SubscriptionId <subscription-id>
```

## Create resource group

```Powershell
New-AzResourceGroup -Name cosmos-devguide-rg -Location 'eastus2'
```

## Deploy using bicep template

Deploy the solution resources using the following command (this will take a few minutes to run):

```Powershell
New-AzResourceGroupDeployment -ResourceGroupName cosmos-devguide-rg -TemplateFile .\azuredeploy.bicep -TemplateParameterFile .\azuredeploy.parameters.json -c
```

> **Enable Vector Search Feature**: This Azure Bicep template will automatically [enable the "Vector Search" feature within Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/vector-search#enroll-in-the-vector-search-preview-feature). If it's not enabled, this Azure PowerShell command can be run to enable it on an Azure Cosmos DB for NoSQL Account:
> ````powershell
> Update-AzCosmosDBAccount -ResourceGroupName <resource-group-name> -Name <account-name> -Capabilities @{name="EnableNoSQLVectorSearch"}
> ````
