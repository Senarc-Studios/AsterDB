__title__ = 'aster.db'
__author__ = 'BenitzCoding'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-present BenitzCoding'
__version__ = '0.0.1'

from .errors import (
   BadRequestError,
   DuplicateError,
   NotFoundError,
   PrivateKeyError,
   ServerError,
   UnknownError
)
from .http import HTTPClient
from .wrapper import (
   Aster,
   # Database,
   # Collection
)