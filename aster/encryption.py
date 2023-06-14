import base64

from .objects import KeyFile

from cryptography.fernet import Fernet

from typing import Union, Any

class Encryption:
    def __init__(self, private_key: Union[str, KeyFile]):
        self.private_key = private_key

    @staticmethod
    def generate_keys():
        key = Fernet.generate_key()
        return key

    def encrypt(self, message: Any) -> bytes:
        encrypted_message: bytes = Fernet(self.private_key).encrypt(message)
        return encrypted_message

    def decrypt_public_key(self, encrypted_message: bytes) -> Any:
        decrypted_message: bytes = Fernet(self.private_key).decrypt(encrypted_message).decode()
        return decrypted_message