# Conclusion

This guide has provided a comprehensive walkthrough for creating intelligent solutions that combine Azure DocumentDB with vector search capabilities powered by DiskANN and document retrieval with Azure OpenAI services to build a chat bot experience.
By integrating these technologies, you can efficiently manage both operational data and vectors within a single database, while leveraging Azure OpenAI for advanced document retrieval and natural language understanding.

The benefits of building a chat bot experience using Azure DocumentDB with vector search capabilities powered by DiskANN and Azure OpenAI services includes:

- **Unified data and vector management**: Storing both operational data and vectors together in a single database reduces complexity, improves performance, and eliminates the need to synchronize data between multiple databases.
- **No need for synchronization**: By keeping data and vectors in one place, you avoid the overhead of synchronizing two different databases.
- **Flexible schema**: Adapt to changing data structures effortlessly, ensuring your system remains flexible and scalable as your application evolves.
- **Support for latency-sensitive applications**: Azure Cosmos DB is optimized for applications requiring low-latency responses, making it suitable for real-time, interactive use cases.
- **High elasticity and throughput**: Azure Cosmos DB can scale seamlessly to handle high-throughput workloads, making it perfect for applications that need to grow dynamically with demand.
- **Store chat history and vector data**: Easily manage chat histories alongside vector and operational data, making it ideal for chat bot and other interactive applications.

We hope you found this guide helpful and informative.

## Clean up

To clean up the resources created in this guide, delete the `mongo-devguide-rg` resource group in the Azure Portal.

Alternatively, you can use the Azure CLI to delete the resource group.
The following command deletes the resource group and all resources within it.
The `--no-wait` flag makes the command return immediately, without waiting for the deletion to complete.

> **Note**: Ensure the Azure CLI session is authenticated using `az login` and the correct subscription is selected using `az account set --subscription <subscription-id>`.

```powershell
az group delete --name mongo-devguide-rg --yes --no-wait
```
