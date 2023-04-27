from .errors import (
    BadRequestError,
    DuplicateError,
    NotFoundError,
    PrivateKeyError,
    ServerError,
    UnknownError
)

import aiohttp # type: ignore
from typing import Optional

RESPONSE_MAP = {
    400: BadRequestError("Bad Request."),
    401: PrivateKeyError("The private key is invalid."),
    404: NotFoundError("The query returned no results."),
    500: ServerError("The server encountered an error.")
}

class HTTPClient:
    def __init__(self, url: str, private_key: str):
        """Initializes the HTTPClient.

        Args:
            url (str): The URL of the AsterDB Server.
            private_key (str): Private key that is used to encrypt and decrypt data.
        """
        self.url = url
        self.private_key = private_key

    async def fetch(self, database: str, collection: str, query: dict, limit: Optional[int] = 0) -> dict:
        """Fetches data with given query.

        Args:
            collection (str): The name of the collection.

        Returns:
            dict: The query result.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}/{database}/{collection}/fetch",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "query": query
                }
            ) as response:
                if response.status == 200:
                    result: dict = await response.json().get("result")
                    result[0] if limit == 1 else (result[:limit] if limit != 0 and limit != 1 else result)
                    return result

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def insert(self, database: str, collection: str, data: dict) -> dict:
        """Inserts data into a collection.

        Args:
            collection (str): The name of the collection.
            data (dict): The data that should be inserted.

        Returns:
            dict: The inserted data.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}/{database}/{collection}/insert",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "data": data
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def update(self, database: str, collection: str, query: dict, data: dict) -> dict:
        """Updates data in a collection.

        Args:
            collection (str): The name of the collection.
            query (dict): The query to find the data.
            data (dict): The data that should be updated.

        Returns:
            dict: The updated data.
        """
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                f"{self.url}/{database}/{collection}/update",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "query": query,
                    "data": data
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def delete(self, database: str, collection: str, query: dict) -> dict:
        """Deletes data in a collection.

        Args:
            collection (str): The name of the collection.
            query (dict): The query to find the data.

        Returns:
            dict: The deleted data.
        """
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f"{self.url}/{database}/{collection}/delete",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "query": query
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def create_collection(self, database: str, collection: str) -> dict:
        """Creates a collection.

        Args:
            collection (str): The name of the collection.

        Returns:
            dict: The created collection.
        """
        async with aiohttp.ClientSession() as session:
            async with session.create(
                f"{self.url}/{database}/create",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "collection": collection
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def delete_collection(self, database: str, collection: str) -> dict:
        """Deletes a collection.

        Args:
            collection (str): The name of the collection.

        Returns:
            dict: The deleted collection.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}/{database}/delete",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "collection": collection
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))

    async def create_database(self, database: str) -> dict:
        """Creates a database.

        Args:
            database (str): The name of the database.

        Returns:
            dict: The created database.
        """
        async with aiohttp.ClientSession() as session:
            async with session.create(
                f"{self.url}/create",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "database": database
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))
            
    async def delete_database(self, database: str) -> dict:
        """Deletes a database.

        Args:
            database (str): The name of the database.

        Returns:
            dict: The deleted database.
        """
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f"{self.url}/delete",
                headers = {
                    "Authorization": self.private_key,
                },
                json = {
                    "database": database
                }
            ) as response:
                if response.status == 200:
                    return await response.json().get("result")

                raise RESPONSE_MAP.get(response.status, UnknownError(f"The server encountered an unknown error: HTTP {response.status}"))