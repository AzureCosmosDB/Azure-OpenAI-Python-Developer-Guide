# Conclusion

This guide was designed to provide an insightful journey for Python/MongoDB developers to get started with vCore-based Azure Cosmos DB for MongoDB as it applies to creating exciting AI-enabled applications using existing skills. We hope you found this guide helpful and informative.

## Clean up

To clean up the resources created in this guide, delete the `mongo-devguide-rg` resource group in the Azure Portal.

Alternatively, you can use the Azure CLI to delete the resource group. The following command deletes the resource group and all resources within it. The `--no-wait` flag makes the command return immediately, without waiting for the deletion to complete.

>**Note**: Ensure the Azure CLI session is authenticated using `az login` and the correct subscription is selected using `az account set --subscription <subscription-id>`.

```powershell
az group delete --name mongo-devguide-rg --yes --no-wait
```
