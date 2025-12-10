# Overview of Azure Cosmos DB

[Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/introduction) is a globally distributed, multi-model database service for both NoSQL and relational workloads.
It supports multiple APIs: NoSQL, MongoDB, PostgreSQL, Cassandra, Gremlin, and Table—covering document, relational, column-family, graph, and key-value data models.
The service offers turnkey global distribution with elastic scaling of throughput and storage.
It delivers single-digit millisecond latencies at the 99th percentile and guarantees high availability through multi-homing capabilities.
Azure Cosmos DB provides comprehensive service level agreements (SLAs) covering throughput, latency, availability, and consistency—a unique combination among cloud database services.

## Azure Cosmos DB and AI

The surge of AI-powered applications has led to the need to integrate data from multiple data stores, introducing another layer of complexity as each data store tends to have its own workflow and operational performance.
Azure Cosmos DB simplifies this process by providing a unified platform for all data types, including AI data.
Azure Cosmos DB supports relational, document, vector, key-value, graph, and table data models, making it an ideal platform for AI applications.
The wide array of data model support combined with guaranteed high availability, high throughput, low latency, and tunable consistency are huge advantages when building these types of applications.

## Azure Cosmos DB for NoSQL

The focus for this developer guide is [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/) and [Vector Search](https://learn.microsoft.com/azure/cosmos-db/nosql/vector-search).

### Azure Cosmos DB for NoSQL capacity modes

Azure Cosmos DB offers three capacity modes: provisioned throughput, serverless and autoscale modes.
When creating an Azure Cosmos DB account, it's essential to evaluate the workload's characteristics in order to choose the appropriate mode to optimize both performance and cost efficiency.

[**Serverless mode**](https://learn.microsoft.com/azure/cosmos-db/serverless) offers a more flexible and pay-as-you-go approach, where only the Request Units consumed are billed.
This is particularly advantageous for applications with sporadic or unpredictable usage patterns, as it eliminates the need to provision resources upfront.

[**Provisioned throughput mode**](https://learn.microsoft.com/azure/cosmos-db/set-throughput) allocates a fixed amount of resources, measured in [Request Units per second (RUs/s)](https://learn.microsoft.com/azure/cosmos-db/request-units), which is ideal for applications with predictable and steady workloads.
This ensures consistent performance and can be more cost-effective when there is a constant or high demand for database operations.
RU/s can be set at both the database and container levels, allowing for fine-grained control over resource allocation.

[**Autoscale mode**](https://learn.microsoft.com/azure/cosmos-db/provision-throughput-autoscale) builds upon the provisioned throughput mode but allows for the database or container automatically and instantly scale up or down resources based on demand, ensuring that the application can handle varying workloads efficiently.
When configuring autoscale, a maximum (Tmax) value threshold is set for a predictable maximum cost.
This mode is suitable for applications with fluctuating usage patterns or infrequently used applications.

[**Dynamic scaling**](https://learn.microsoft.com/azure/cosmos-db/autoscale-per-partition-region) allows for the automatic and independent scaling of non-uniform workloads across regions and partitions according to usage patterns.
For instance, in a disaster recovery configuration with two regions, the primary region may experience high traffic while the secondary region can scale down to idle, thereby saving costs.
This approach is also highly effective for multi-regional applications, where traffic patterns fluctuate based on the time of day in each region.
