from .errors import (
    BadRequestError,
    DuplicateError,
    NotFoundError,
    PrivateKeyError,
    ServerError,
    UnknownError
)

import aiohttp
from typing import Optional

class Requests:
    def __init__(self, url: str, private_key: str):
        """Initializes the Requests.

        Args:
            url (str): The URL of the AsterDB Server.
            private_key (str): Private key that is used to encrypt and decrypt data.
        """
        self.url = url
        self.private_key = private_key

    async def fetch(self, database: str, collection: str, query: dict, limit: Optional[int] = 0):
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

                elif response.status == 400:
                    raise BadRequestError("The request was invalid.")

                elif response.status == 401:
                    raise PrivateKeyError("The private key is invalid.")

                elif response.status == 404:
                    raise NotFoundError("The query returned no results.")

                elif response.status == 500:
                    raise ServerError("The server encountered an error.")

                else:
                    return UnknownError(f"The server encountered an unknown error: HTTP {response.status}")

    async def insert(self, database: str, collection: str, data: dict):
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
                    return await response.json()

                elif response.status == 400:
                    if await response.json() == {"error": "duplicate"}:
                        raise DuplicateError("The data is already in the collection.")

                    else:
                        raise BadRequestError("The request was invalid.")

                elif response.status == 401:
                    raise PrivateKeyError("The private key is invalid.")

                elif response.status == 404:
                    raise NotFoundError("The collection or database was not found.")

                elif response.status == 500:
                    raise ServerError("The server encountered an error.")

                else:
                    return UnknownError(f"The server encountered an unknown error: HTTP {response.status}")

    async def update(self, database: str, collection: str, query: dict, data: dict):
        """Updates data in a collection.

        Args:
            collection (str): The name of the collection.
            query (dict): The query to find the data.
            data (dict): The data that should be updated.

        Returns:
            dict: The updated data.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
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
                    return await response.json()

                elif response.status == 400:
                    raise BadRequestError("The request was invalid.")

                elif response.status == 401:
                    raise PrivateKeyError("The private key is invalid.")

                elif response.status == 404:
                    raise NotFoundError("The collection or database was not found.")

                elif response.status == 500:
                    raise ServerError("The server encountered an error.")

                else:
                    return UnknownError(f"The server encountered an unknown error: HTTP {response.status}")