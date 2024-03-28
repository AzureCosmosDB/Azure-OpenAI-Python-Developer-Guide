# Load data into Azure Cosmos DB API for MongoDB

The previous lab demonstrated how to add data to a collection individually. This lab will demonstrate how to load data using bulk operations into multiple collections. This data will be used in subsequent labs to explain further the capabilities of Azure Cosmos DB API for MongoDB about AI.

When loading data, bulk operations are preferred over adding each document individually. Bulk operations involve performing multiple database operations as a batch rather than executing them simultaneously. This approach is more efficient and provides several benefits:

1. Performance: By issuing load operations in bulk, the lab can significantly reduce the overhead of network round-trips and database operations. This results in faster data loading and improved overall performance.

2. Scalability: Bulk operations allow the lab to handle large volumes of data efficiently. They can quickly process and load a substantial amount of customer, product, and sales data, enabling them to scale their operations as needed.

3. Atomicity: Bulk operations ensure that all database changes within a batch are treated as a single transaction. The entire batch can be rolled back if any document fails to load, maintaining data integrity and consistency.

4. Simplified code logic: By using bulk operations, the lab can simplify its code logic and reduce the number of database queries. This results in cleaner, more manageable code and reduces the likelihood of errors or inconsistencies.

## Lab - Load data into Azure Cosmos DB API for MongoDB collections

This lab will load the Cosmic Works Customer, Product, and Sales data into Azure Cosmos DB API for MongoDB collections using bulk operations. Both the Azure Cosmos DB Emulator and Azure Cosmos DB account in Azure are supported for completion of this lab.

>**Note**: It is highly recommended to use a [virtual environment](https://python.land/virtual-environments/virtualenv) for all labs.

Please visit the lab repository to complete [this lab](https://github.com/AzureCosmosDB/Azure-OpenAI-Python-Developer-Guide/blob/main/Labs/lab_2_load_data.ipynb).

This lab demonstrates the use of bulk operations to load product, customer, and sales data into Azure Cosmos DB API for MongoDB collections. As an example, the following code snippet inserts product data using the `bulk_write` method allowing for upsert functionality using the `UpdateOne` method:

```python
# Add product data to database using bulkwrite and updateOne with upsert
# Get cosmic works product data from github
product_raw_data = "https://cosmosdbcosmicworks.blob.core.windows.net/cosmic-works-small/product.json"
product_data = ProductList(items=[Product(**data) for data in requests.get(product_raw_data).json()])
db.products.bulk_write([ UpdateOne({"_id": prod.id}, {"$set": prod.model_dump(by_alias=True)}, upsert=True) for prod in product_data.items])
```
