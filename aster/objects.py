from typing import Optional

class DirectLink:
    def __init__(self, mongo_uri: str):
        """Initializes the DirectLink.

        Args:
            mongo_uri (str): The URI of the MongoDB server.
        """
        if not mongo_uri.startswith("mongodb://") or not mongo_uri.startswith("mongodb+srv://"):
            raise ValueError("Invalid MONGO URI provided.")

        else:
            self.mongo_uri = mongo_uri

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