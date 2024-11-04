# Overview of Azure Cosmos DB

[Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/introduction) is a globally distributed, multi-model database service that enables querying and storing data using NoSQL models using one of five APIs: SQL (document database), Cassandra (column-family), MongoDB (document database), Azure Table, and graph database. It provides turnkey global distribution, elastic scaling of throughput and storage worldwide, single-digit millisecond latencies at the 99th percentile, and guaranteed high availability with multi-homing capabilities. Azure Cosmos DB provides comprehensive service level agreements (SLAs) for throughput, latency, availability, and consistency guarantees, something not found in any other database service.

## Azure Cosmos DB and AI

The surge of AI-powered applications has led to the need to integrate data from multiple data stores, introducing another layer of complexity as each data store tends to have its own workflow and operational performance. Azure Cosmos DB simplifies this process by providing a unified platform for all data types, including AI data. Azure Cosmos DB supports relational, document, vector, key-value, graph, and table data models, making it an ideal platform for AI applications. The wide array of data model support combined with guaranteed high availability, high throughput, low latency, and tunable consistency are huge advantages when building these types of applications.

## Azure Cosmos DB for Mongo DB

The focus for this developer guide is [Azure Cosmos DB for MongoDB](https://learn.microsoft.com/azure/cosmos-db/mongodb/introduction). Developers can leverage their current MongoDB expertise and use their preferred MongoDB drivers, SDKs, and tools simply by directing applications to the connection string for on the Azure Cosmos DB for MongoDB account.

### Azure Cosmos DB for Mongo DB API Architectures

The [RU architecture](https://learn.microsoft.com/azure/cosmos-db/mongodb/ru/introduction) for Azure Cosmos DB for MongoDB offers instantaneous scalability with zero warmup period, automatic and transparent sharding, and 99.999% availability. It supports active-active databases across multiple regions, cost-efficient, granular, unlimited scalability, real-time analytics, and serverless deployments paying only per operation.

[vCore-based Azure Cosmos DB for MongoDB architecture](https://learn.microsoft.com/azure/cosmos-db/mongodb/vcore/introduction) integrates AI-based applications with private organizational data, with text indexing for easy querying. Simplify the development process with high-capacity vertical scaling and free 35-day backups with a point-in-time restore (PITR).

The [choice between vCore and Request Units (RU)](https://learn.microsoft.com/azure/cosmos-db/mongodb/choose-model) in Azure Cosmos DB for MongoDB API depends on the workload. A list of [compatibility and feature support between RU and vCore](https://learn.microsoft.com/azure/cosmos-db/mongodb/vcore/compatibility) is available.

vCore provides predictable performance and cost and is ideal for running high-performance, mission-critical workloads with low latency and high throughput. With vCore, the number of vCPUs and the memory the database needs is configurable and can be scaled up or down as needed.

Conversely, RU is a consumption-based model that charges based on the number of operations the database performs, including reads, writes, and queries. RU is ideal for scenarios where the workload has unpredictable traffic patterns or a need to optimize cost for bursty workloads.

A steady-state workload with predictable traffic patterns is best suited for vCore since it provides more predictable performance and cost. However, RU may be a better choice if the workload has unpredictable traffic patterns or requires bursty performance since it allows for paying only for the resources used.

>**NOTE**: AI-supporting workloads, such as vector search, must use the vCore architecture, as vector search is not supported with RU accounts.
