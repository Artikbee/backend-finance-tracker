class ApplicationError(Exception):
    @property
    def message(self) -> str:
        return "Application error occurred"


class AuthenticationError(ApplicationError):
    """
    401 - HTTP status code
    """
    ...


class ConflictError(ApplicationError):
    """
    409 - HTTP status code
    """
    ...


class NotFoundError(ApplicationError):
    """
    404 - HTTP status code
    """
    ...
