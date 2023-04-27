from .objects import KeyFile, DirectLink
from .wrapper import DirectLink

from typing import Union, Optional
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
from base64 import b64decode

from Crypto.PublicKey import RSA # type: ignore
from Crypto.Signature import PKCS1_v1_5 # type: ignore

class AsterClient:
    def __init__(self, mongo_uri: DirectLink, private_key: Optional[Union[str, KeyFile]] = None):
        """Initializes the Client.

        Args:
            mongo_uri (DirectLink): The MongoDB URI.
        """
        self.mongo_uri = mongo_uri
        self.mongo_client = AsyncIOMotorClient(self.mongo_uri)
        self.private_key = KeyFile().load_key(private_key)

    async def fetch(self, database: Optional[str], collection: Optional[str], query: dict) -> dict:
        """Fetches data from the database.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            query (dict): The query.

        Returns:
            dict: The query result.
        """
        if database is None:
            raise ValueError("No database provided.")

        elif collection is None:
            raise ValueError("No collection provided.")

        else:
            db = self.mongo_client[database]
            col = db[collection]

            rsa_key = RSA.importKey(self.private_key)
            cipher = PKCS1_v1_5.new(rsa_key)
            document = await col.find_one(query)
            decrypted_data: dict = {}
            for key, value in document.items():
                raw_cipher_key = b64decode(key)
                raw_cipher_value = b64decode(value)
                decrypted_key = cipher.decrypt(raw_cipher_key, None)
                decrypted_value = cipher.decrypt(raw_cipher_value, None)
                decrypted_data.update(
                    {
                        decrypted_key: decrypted_value
                    }
                )

            return decrypted_data

    async def insert(self, database: Optional[str], collection: Optional[str], data: dict) -> dict:
        """Inserts data into the database.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            data (dict): The data.

        Returns:
            dict: The query result.
        """
        if database is None:
            raise ValueError("No database provided.")

        elif collection is None:
            raise ValueError("No collection provided.")

        else:
            db = self.mongo_client[database]
            col = db[collection]

            rsa_key = RSA.importKey(self.private_key)
            cipher = PKCS1_v1_5.new(rsa_key)
            encrypted_data: dict = {}
            for key, value in data.items():
                encrypted_key = cipher.encrypt(key.encode())
                encrypted_value = cipher.encrypt(value.encode())
                encrypted_data.update(
                    {
                        encrypted_key: encrypted_value
                    }
                )
            return await col.insert_one(encrypted_data)

    async def update(self, database: Optional[str], collection: Optional[str], query: dict, data: dict) -> dict:
        """Updates data in the database.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            query (dict): The query.
            data (dict): The data.

        Returns:
            dict: The query result.
        """
        if database is None:
            raise ValueError("No database provided.")

        elif collection is None:
            raise ValueError("No collection provided.")

        else:
            db = self.mongo_client[database]
            col = db[collection]
            return await col.update_one(query, data)

    async def delete(self, database: Optional[str], collection: Optional[str], query: dict) -> dict:
        """Deletes data from the database.

        Args:
            database (str, optional): The name of the database.
            collection (str, optional): The name of the collection.
            query (dict): The query.

        Returns:
            dict: The query result.
        """
        if database is None:
            raise ValueError("No database provided.")

        elif collection is None:
            raise ValueError("No collection provided.")

        else:
            db = self.mongo_client[database]
            col = db[collection]
            return await col.delete_one(query)