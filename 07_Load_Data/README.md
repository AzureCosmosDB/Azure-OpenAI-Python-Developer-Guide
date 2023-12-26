# Load data into Azure Cosmos DB API for MongoDB

Lab 1 demonstrated how to add data to a collection individually. This lab will demonstrate how to load data using bulk operations into multiple collections. This data will be used in subsequent labs to explain further the capabilities of Azure Cosmos DB API for MongoDB about AI.

When loading data, bulk operations are preferred over adding each document individually. Bulk operations involve performing multiple database operations as a batch rather than executing them simultaneously. This approach is more efficient and provides several benefits:

1. Performance: By issuing load operations in bulk, the lab can significantly reduce the overhead of network round-trips and database operations. This results in faster data loading and improved overall performance.

2. Scalability: Bulk operations allow the lab to handle large volumes of data efficiently. They can quickly process and load a substantial amount of customer, product, and sales data, enabling them to scale their operations as needed.

3. Atomicity: Bulk operations ensure that all database changes within a batch are treated as a single transaction. The entire batch can be rolled back if any document fails to load, maintaining data integrity and consistency.

4. Simplified code logic: By using bulk operations, the lab can simplify its code logic and reduce the number of database queries. This results in cleaner, more manageable code and reduces the likelihood of errors or inconsistencies.

## Lab 2 - Load data into Azure Cosmos DB API for MongoDB collections

This lab will load the Cosmic Works Customer, Product, and Sales data into Azure Cosmos DB API for MongoDB collections using bulk operations.

Please complete Lab 2 in the lab repository.
