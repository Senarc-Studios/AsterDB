class ServerError(Exception):
    """Raised when the server has an exception."""

class TimeoutError(Exception):
    """Raised when the server times out."""

class DuplicateError(Exception):
    """Raised when the data is already in the collection."""

class BadRequestError(Exception):
    """Raised when the request is invalid."""

class PrivateKeyError(Exception):
    """Raised when the private key is invalid."""

class NotFoundError(Exception):
    """Raised when the collection or database was not found."""

class UnknownError(Exception):
    """Raised when the server has an unknown error."""