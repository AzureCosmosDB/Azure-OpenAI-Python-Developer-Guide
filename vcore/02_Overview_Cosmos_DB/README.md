# Overview of Azure Cosmos DB

[Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/introduction) is Microsoft's cloud-native, serverless NoSQL and vector database for mission-critical and globally distributed applications. It provides a native JSON document model with a SQL-like query language, combining flexible data modeling with familiar query semantics. With built-in vector search capabilities, Azure Cosmos DB enables AI-powered scenarios such as semantic search, retrieval-augmented generation, and intelligent applications. As an Azure-native service, it integrates deeply with Azure and delivers predictable performance and availability backed by industry-leading service level agreements (SLAs).
The service offers turnkey global distribution with elastic scaling of throughput and storage.
It delivers single-digit millisecond latencies at the 99th percentile and guarantees high availability through multi-homing capabilities.
Azure Cosmos DB provides comprehensive SLAs covering throughput, latency, availability, and consistency—a unique combination among cloud database services.

## Azure Cosmos DB and AI

The surge of AI-powered applications has led to the need to integrate data from multiple data stores, introducing another layer of complexity as each data store tends to have its own workflow and operational performance.
Azure Cosmos DB simplifies this process by providing a unified platform for document and vector data.
Azure Cosmos DB provides a native JSON document model combined with built-in vector search capabilities, making it an ideal platform for AI applications.
This document and vector support combined with guaranteed high availability, high throughput, low latency, and tunable consistency are huge advantages when building these types of applications.

## Azure DocumentDB

The focus for this developer guide is [Azure DocumentDB](https://learn.microsoft.com/azure/documentdb/overview).
Azure DocumentDB (previously known as vCore-based Azure Cosmos DB for MongoDB) is a fully managed MongoDB-compatible database service optimized for modern application development.
Developers can apply their existing MongoDB expertise and continue using their preferred MongoDB drivers, SDKs, and tools by simply pointing applications to the Azure DocumentDB connection string.

### Azure DocumentDB Architecture

Azure DocumentDB is powered by the open-source [DocumentDB engine](https://github.com/documentdb/documentdb), which is built on PostgreSQL and provides full MongoDB wire protocol compatibility.
This open-source foundation, released under the permissive MIT license, gives developers complete transparency and flexibility.

The service provides flexible and scalable data management with a schema-agnostic design.
It supports both vertical and horizontal scaling to handle high-capacity workloads, with no shard key required until your database surpasses terabytes.
You can shard existing databases automatically with no downtime and scale clusters up or down without interrupting your applications.
For more information, see [Azure DocumentDB scalability and architecture](https://learn.microsoft.com/azure/documentdb/scalability-overview).

Azure DocumentDB includes an [integrated vector database](https://learn.microsoft.com/azure/documentdb/vector-search) that enables you to store, index, and query high-dimensional vector data alongside your original data.
This eliminates the need to replicate data in a separate vector database, reducing cost and complexity while enabling AI-powered applications such as semantic search, recommendations, and retrieval-augmented generation (RAG).
