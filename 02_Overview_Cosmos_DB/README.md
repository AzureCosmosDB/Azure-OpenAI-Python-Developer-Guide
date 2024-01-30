# Overview of Azure Cosmos DB

[Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction) is a globally distributed, multi-model database service that enables you to query and store data using NoSQL models using one of five APIs: SQL (document database), Cassandra (column-family), MongoDB (document database), Azure Table, and Gremlin (graph database). It provides turnkey global distribution, elastic scaling of throughput and storage worldwide, single-digit millisecond latencies at the 99th percentile, and guaranteed high availability with multi-homing capabilities. Azure Cosmos DB provides comprehensive service level agreements (SLAs) for throughput, latency, availability, and consistency guarantees, something not found in any other database service.

## Azure Cosmos DB for Mongo DB

[Azure Cosmos DB for MongoDB](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/introduction) simplifies utilizing Azure Cosmos DB as a MongoDB database. You can leverage your current MongoDB expertise and still use your preferred MongoDB drivers, SDKs, and tools simply by directing your application to the connection string for your account.

### Azure Cosmos DB for Mongo DB API Architectures

The [RU architecture](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/ru/introduction) for Azure Cosmos DB for MongoDB offers instantaneous scalability with zero warmup period, automatic and transparent sharding, and 99.999% availability. It supports active-active databases across multiple regions, cost-efficient, granular, unlimited scalability, real-time analytics, and serverless deployments where you pay only per operation.

Azure Cosmos DB for MongoDB [vCore architecture](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/introduction) integrates AI-based applications with your data, with text indexing for easy querying. Simplify your development process with high-capacity vertical scaling and free 35-day backups with a point-in-time restore (PITR).

The [choice between vCore and Request Units (RU)](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/choose-model) in Azure Cosmos DB for MongoDB API depends on the workload. A list of [compatibility and feature support between RU and vCore](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/compatibility) is available.

vCore provides predictable performance and cost and is ideal for running high-performance, mission-critical workloads with low latency and high throughput. With vCore, the number of vCPUs and the memory the database needs is configurable and can be scaled up or down as needed.

Conversely, RU is a consumption-based model that charges based on the number of operations the database performs, including reads, writes, and queries. RU is ideal for scenarios where the workload has unpredictable traffic patterns or a need to optimize cost for bursty workloads.

A steady-state workload with predictable traffic patterns is best suited for vCore since it provides more predictable performance and cost. However, RU may be a better choice if the workload has unpredictable traffic patterns or requires bursty performance since it allows you to pay only for the resources used.

>**NOTE**: AI-supporting workloads, such as vector search, must use vCore, as vector search is not supported with RU accounts.
