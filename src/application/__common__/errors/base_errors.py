from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationError(Exception):
    @property
    def message(self) -> str:
        return "Application error occurred"


@dataclass(eq=False)
class AuthenticationError(ApplicationError):
    """
    401 - HTTP status code
    """
    ...


@dataclass(eq=False)
class ConflictError(ApplicationError):
    """
    409 - HTTP status code
    """
    ...


@dataclass(eq=False)
class NotFoundError(ApplicationError):
    """
    404 - HTTP status code
    """
    ...
