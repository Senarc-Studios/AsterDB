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
            private_key (str, key, optional): Private key that is used to encrypt and decrypt data. Defaults to None.
        """
        self.url = url
        self.private_key = KeyFile().load_key(private_key)
        self.client = Requests(self.url, self.private_key)

    def set_key(self, private_key: Union[str, KeyFile]):
        """Sets the private key.

        Args:
            private_key (str, key): The private key.
        """
        self.private_key = KeyFile().load_key(private_key)

    def set_database(self, database: str):
        """Sets the database.

        Args:
            database (str): The database.
        """
        self.database = database

    def set_collection(self, collection: str):
        """Sets the collection.

        Args:
            collection (str): The collection.
        """
        self.collection = collection

    async def get(self, database: Optional[str], collection: Optional[str], query: dict):
        """Gets a collection.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.

        Returns:
            dict: The query result.
        """
        return await self.client.get(database, collection, query)