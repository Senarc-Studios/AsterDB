from .http import Requests

from typing import Union, Optional

class KeyFile:
    def __init__(self, path: Optional[str] = None):
        """Initializes the KeyFile.

        Args:
            path (str): The path to the key file.
        """
        with open(path, "r") as file:
            self.key = file.read()

    def load_key(self) -> str:
        """Loads the key from the key file.

        Returns:
            str: The key.
        """
        return self.key

class Aster:
    def __init__(self, url: str, private_key: Optional[Union[str, KeyFile]] = None):
        """Initializes the Wrapper.

        Args:
            url (str): The URL of the AsterDB Server.
            private_key (str, KeyFile, optional): Private key that is used to encrypt and decrypt data. Defaults to None.
        """
        self.url = url
        self.private_key = KeyFile().load_key(private_key)
        self.client = Requests(self.url, self.private_key)

    def set_key(self, private_key: Union[str, KeyFile]) -> Union[str, KeyFile]:
        """Sets the private key.

        Args:
            private_key (str, key): The private key.
        """
        self.private_key = KeyFile().load_key(private_key)
        return self.private_key

    def set_database(self, database: str) -> str:
        """Sets the database.

        Args:
            database (str): The database.
        """
        self.database = database
        return self.database

    def set_collection(self, collection: str) -> str:
        """Sets the collection.

        Args:
            collection (str): The collection.
        """
        self.collection = collection
        return self.collection

    async def get(self, database: Optional[str], collection: Optional[str], query: dict) -> dict:
        """Gets a collection.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.

        Returns:
            dict: The query result.
        """
        return await self.client.fetch(database, collection, query)

    async def insert(self, database: Optional[str], collection: Optional[str], data: dict) -> dict:
        """Inserts data into a collection.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            data (dict): The data that should be inserted.

        Returns:
            dict: The inserted data.
        """
        return await self.client.insert(database, collection, data)

    async def update(self, database: Optional[str], collection: Optional[str], query: dict, data: dict) -> dict:
        """Updates data in a collection.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            query (dict): The query that should be used to find the data.
            data (dict): The data that should be updated.

        Returns:
            dict: The updated data.
        """
        return await self.client.update(database, collection, query, data)

    async def delete(self, database: Optional[str], collection: Optional[str], query: dict) -> dict:
        """Deletes data in a collection.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            query (dict): The query that should be used to find the data.

        Returns:
            dict: The deleted data.
        """
        return await self.client.delete(database, collection, query)

    async def create_database(self, database: str) -> dict:
        """Creates a database.

        Args:
            database (str): The name of the database.
        """
        return await self.client.create_database(database)

    async def create_collection(self, database: str, collection: str) -> dict:
        """Creates a collection.

        Args:
            database (str): The name of the database.
            collection (str): The name of the collection.
        """
        return await self.client.create_collection(database, collection)

    async def delete_database(self, database: str):
        """Deletes a database.

        Args:
            database (str): The name of the database.
        """
        return await self.client.delete_database(database)

    async def delete_collection(self, database: str, collection: str) -> dict:
        """Deletes a collection.

        Args:
            database (str): The name of the database.
            collection (str): The name of the collection.
        """
        return await self.client.delete_collection(database, collection)