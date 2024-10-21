# Overview of Azure Cosmos DB

[Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/introduction) is a globally distributed database for storing and querying both NoSQL and vector data, with a serverless option. It has multiple APIs, the most notable being the native NoSQL document API and MongoDB API. It provides turnkey global distribution, elastic and dynamic scaling of throughput and storage, and a comprehensive SLA (service level agreement) for single-digit millisecond latency and 99.999% high-availability.

## Azure Cosmos DB and AI

The surge of AI-powered applications has led to the need to integrate data from multiple data stores, introducing another layer of complexity as each data store tends to have its own workflow and operational performance. Azure Cosmos DB simplifies this process by providing a unified platform for all data types, including AI data. In particular, its support for vector storage and retrieval is a game-changer for generative AI applications. By representing complex data elements like text, images, or sound as high-dimensional vectors, Azure Cosmos DB allows for efficient storage, indexing, and querying of these vectors, which is crucial for many generative AI tasks.

Unlike traditional databases requiring separate workarounds for different data types, Azure Cosmos DB supports multiple data models within a single, integrated environment. This simplification means you can leverage the same robust platform for all your AI data needs. Many AI applications rely on external stand-alone vector stores, which can be cumbersome to manage and maintain. Azure Cosmos DB's native support for vector storage and retrieval eliminates the need for these external stores as all the application's data is located in a single place thus streamlining the development and deployment of AI applications. These features enable the building, deploying, and scaling of AI applications to be more efficient and reliable, making Azure Cosmos DB an ideal choice for handling the complex data requirements of modern generative AI solutions.

## Azure Cosmos DB for NoSQL

The focus for this developer guide is [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/) and [Vector Search](https://learn.microsoft.com/azure/cosmos-db/nosql/vector-search).

### Azure Cosmos DB for NoSQL capacity modes

Azure Cosmos DB offers three capacity modes: provisioned throughput, serverless and autoscale modes. creating an Azure Cosmos DB account, it's essential to evaluate the workload's characteristics in order to choose the appropriate mode to optimize both performance and cost efficiency.

[**Serverless mode**](https://learn.microsoft.com/en-us/azure/cosmos-db/serverless) offers a more flexible and pay-as-you-go approach, where only the Request Units consumed are billed. This is particularly advantageous for applications with sporadic or unpredictable usage patterns, as it eliminates the need to provision resources upfront.

[**Provisioned throughput mode**](https://learn.microsoft.com/azure/cosmos-db/set-throughput) allocates a fixed amount of resources, measured in [Request Units per second (RUs/s)](https://learn.microsoft.com/azure/cosmos-db/request-units), which is ideal for applications with predictable and steady workloads. This ensures consistent performance and can be more cost-effective when there is a constant or high demand for database operations. RU/s can be set at both the database and container levels, allowing for fine-grained control over resource allocation.

[**Autoscale mode**](https://learn.microsoft.com/azure/cosmos-db/provision-throughput-autoscale) builds upon the provisioned throughput mode but allows for the database or container automatically and instantly scale up or down resources based on demand, ensuring that the application can handle varying workloads efficiently. When configuring autoscale, a maximum (Tmax) value threshold is set for a predictable maximum cost. This mode is suitable for applications with fluctuating usage patterns or infrequently used applications.

[**Dynamic scaling**](https://learn.microsoft.com/en-us/azure/cosmos-db/autoscale-per-partition-region) allows for the automatic and independent scaling of non-uniform workloads across regions and partitions according to usage patterns. For instance, in a disaster recovery configuration with two regions, the primary region may experience high traffic while the secondary region can scale down to idle, thereby saving costs. This approach is also highly effective for multi-regional applications, where traffic patterns fluctuate based on the time of day in each region.
