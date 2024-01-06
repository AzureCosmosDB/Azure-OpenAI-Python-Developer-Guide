# Solution deployment

## Prerequisites

- Owner on Azure subscription
- Account approved for Azure OpenAI service
- Azure CLI installed
- Azure PowerShell installed

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
New-AzResourceGroup -Name mongo-devguide-rg -Location 'eastus'
```

## Deploy using bicep template

Deploy the solution resources using the following command (this will take a few minutes to run):

```Powershell
New-AzResourceGroupDeployment -ResourceGroupName mongo-devguide-rg -TemplateFile .\azuredeploy.bicep -TemplateParameterFile .\azuredeploy.parameters.json -c
```
