from functools import partial

from fastapi import FastAPI
from starlette import status

from application.__common__.errors.base_errors import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
)
from domains.__common__.base_errors import FieldError
from infrastructure.__common__.errors.jwt_error import JWTError
from presentation.http.v1.__common__.exc_handlers import validate


def setup_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        AuthenticationError,
        partial(validate, status=status.HTTP_401_UNAUTHORIZED),
    )
    app.add_exception_handler(
        JWTError,
        partial(validate, status=status.HTTP_401_UNAUTHORIZED),
    )
    app.add_exception_handler(
        NotFoundError,
        partial(validate, status=status.HTTP_404_NOT_FOUND),
    )
    app.add_exception_handler(
        ConflictError,
        partial(validate, status=status.HTTP_409_CONFLICT),
    )
    app.add_exception_handler(
        FieldError,
        partial(validate, status=status.HTTP_422_UNPROCESSABLE_ENTITY),
    )
