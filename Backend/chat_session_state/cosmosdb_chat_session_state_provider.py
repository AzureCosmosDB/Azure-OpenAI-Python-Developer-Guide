import os
from datetime import datetime
from typing import List, Optional
from azure.cosmos import CosmosClient, PartitionKey, exceptions as cosmos_exceptions
from dotenv import load_dotenv

from api_models.chat_session_request import ChatSessionResponse
from api_models.chat_session import ChatSession

# Load environment variables
load_dotenv()

# Initialize Cosmos DB client and container globally within the module
CONNECTION_STRING = os.environ.get("COSMOS_DB_CONNECTION_STRING")
client = CosmosClient.from_connection_string(CONNECTION_STRING)
db = client.get_database_client("cosmic_works")

# Initialize the chat session container, create if not exists
db.create_container_if_not_exists(id="chat_session", partition_key=PartitionKey(path="/id"))

chat_session_container = db.get_container_client("chat_session")


class CosmosDBChatSessionStateProvider:
    """
    A class to encapsulate CRUD operations for interacting with the chat session state in Cosmos DB.
    """

    def __init__(self, container=chat_session_container):
        self.container = container

    def list_sessions(self) -> List[ChatSessionResponse]:
        """
        Lists all chat sessions from the chat session container.

        Returns:
            List[ChatSessionResponse]: A list of chat session responses.
        """
        try:
            query = "SELECT c.id, c.title FROM c"
            sessions = list(self.container.query_items(
                query=query,
                enable_cross_partition_query=True
            ))

            # Convert the sessions into a list of ChatSessionResponse objects
            session_responses = [
                ChatSessionResponse(session_id=session['id'], title=session['title'])
                for session in sessions
            ]
            return session_responses
        except cosmos_exceptions.CosmosHttpResponseError as e:
            raise RuntimeError(f"Failed to retrieve sessions: {str(e)}")

    def load_or_create_chat_session(self, session_id: str) -> ChatSession:
        """
        Load an existing session from the Cosmos DB container, or create a new one if not found.
        """
        try:
            # Try to read the session from Cosmos DB
            session_item = chat_session_container.read_item(item=session_id, partition_key=session_id)
            return ChatSession(**session_item)
        except Exception:
            # If the session is not found, create a new one
            new_session = ChatSession(
                id=session_id,
                session_id=session_id,
                title=f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}",
                chat_history=[]
            )
            chat_session_container.upsert_item(new_session.model_dump())
            return new_session
        
    def load_session(self, session_id: str) -> Optional[dict]:
        """
        Loads a chat session by session ID.

        Args:
            session_id (str): The ID of the session to be loaded.

        Returns:
            Optional[dict]: The chat session data if found, else None.
        """
        try:
            query = f"SELECT * FROM c WHERE c.id = '{session_id}'"
            session = list(self.container.query_items(
                query=query,
                enable_cross_partition_query=True
            ))

            if session:
                return session[0]
            else:
                raise ValueError("Session not found")
        except cosmos_exceptions.CosmosHttpResponseError as e:
            raise RuntimeError(f"Failed to retrieve session: {str(e)}")

    def upsert_session(self, session: ChatSession) -> dict:
        """
        Creates or updates a chat session in the chat session container.

        Args:
            session: The chat session to create or update.

        Returns:
            dict: The upserted session data.
        """
        try:
            response = self.container.upsert_item(session.model_dump())
            return response
        except cosmos_exceptions.CosmosHttpResponseError as e:
            raise RuntimeError(f"Failed to create or update session: {str(e)}")

    # def delete_session(self, session_id: str) -> None:
    #     """
    #     Deletes a chat session by session ID.

    #     Args:
    #         session_id (str): The ID of the session to delete.
    #     """
    #     try:
    #         self.container.delete_item(item=session_id, partition_key=session_id)
    #     except cosmos_exceptions.CosmosResourceNotFoundError:
    #         raise ValueError(f"Session with ID '{session_id}' not found")
    #     except cosmos_exceptions.CosmosHttpResponseError as e:
    #         raise RuntimeError(f"Failed to delete session: {str(e)}")
