from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

CredentialsDependency = Annotated[
    HTTPAuthorizationCredentials,
    Depends(HTTPBearer())
]
