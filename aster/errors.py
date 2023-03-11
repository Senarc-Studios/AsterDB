class ServerError(Exception):
    """Raised when the server has an exception."""
    pass

class TimeoutError(Exception):
    """Raised when the server times out."""
    pass

class DuplicateError(Exception):
    """Raised when the data is already in the collection."""
    pass

class BadRequestError(Exception):
    """Raised when the request is invalid."""
    pass

class PrivateKeyError(Exception):
    """Raised when the private key is invalid."""
    pass

class NotFoundError(Exception):
    """Raised when the collection or database was not found."""
    pass

class UnknownError(Exception):
    """Raised when the server has an unknown error."""
    pass