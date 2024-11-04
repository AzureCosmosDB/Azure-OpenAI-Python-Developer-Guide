
import time
import json
from langchain_core.retrievers import BaseRetriever
from langchain_openai import AzureOpenAIEmbeddings
from azure.cosmos import ContainerProxy
from pydantic import BaseModel
from typing import Type, TypeVar, List
from langchain_core.callbacks import (
    AsyncCallbackManagerForRetrieverRun,
    CallbackManagerForRetrieverRun,
)
from langchain_core.documents import Document


T = TypeVar('T', bound=BaseModel)

class AzureCosmosDBNoSQLRetriever(BaseRetriever):
    """
    A custom LangChain retriever that uses Azure Cosmos DB NoSQL database for vector search.
    """
    embedding_model: AzureOpenAIEmbeddings
    container: ContainerProxy
    model: Type[T]
    vector_field_name: str
    num_results: int=5

    def __get_embeddings(self, text: str) -> List[float]:       
        """
        Returns embeddings vector for a given text.
        """
        embedding = self.embedding_model.embed_query(text)        
        time.sleep(0.5) # rest period to avoid rate limiting on AOAI
        return embedding
    
    def __get_item_by_id(self, id) -> T:
        """
        Retrieves a single item from the Azure Cosmos DB NoSQL database by its ID.
        """
        query = "SELECT * FROM itm WHERE itm.id = @id"
        parameters = [
            {"name": "@id", "value": id}
        ]    
        item = list(self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))[0]
        return self.model(**item)
    
    def __delete_attribute_by_alias(self, instance: BaseModel, alias):
        for model_field in instance.model_fields:
            field = instance.model_fields[model_field]            
            if field.alias == alias:
                delattr(instance, model_field)
                return
    
    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """
        Performs a synchronous vector search on the Azure Cosmos DB NoSQL database.
        """
        embedding = self.__get_embeddings(query)
        items = self.container.query_items(
            query=f"""SELECT TOP @num_results itm.id, VectorDistance(itm.{self.vector_field_name}, @embedding) AS SimilarityScore 
                    FROM itm
                    ORDER BY VectorDistance(itm.{self.vector_field_name}, @embedding)
                    """,
            parameters = [
                { "name": "@num_results", "value": self.num_results },
                { "name": "@embedding", "value": embedding }            
            ],
            enable_cross_partition_query=True
        ) 
        returned_docs = []
        for item in items:
            itm = self.__get_item_by_id(item["id"])  
            # Remove the vector field from the returned item so it doesn't fill the context window
            self.__delete_attribute_by_alias(itm, self.vector_field_name)            
            returned_docs.append(Document(page_content=json.dumps(itm, indent=4, default=str), metadata={"similarity_score": item["SimilarityScore"]}))
        return returned_docs
    
    async def _aget_relevant_documents(
        self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun
    ) -> List[Document]:
        """
        Performs an asynchronous vector search on the Azure Cosmos DB NoSQL database.        
        """
        raise Exception(f"Asynchronous search not implemented.")