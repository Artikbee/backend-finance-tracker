class ApplicationError(Exception):
    @property
    def message(self) -> str:
        return "Application error occurred"


class ConflictError(ApplicationError):
    """
    409 - HTTP status code
    Request conflict with the current state of the target resource.
    """
    ...


class NotFoundError(ApplicationError):
    """
    404 - HTTP status code
    """
    ...
