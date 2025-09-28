from dataclasses import dataclass

from application.__common__.errors.base_errors import ConflictError


@dataclass(eq=False)
class UserAlreadyExistsError(ConflictError):
    @property
    def message(self) -> str:
        return "User already exists"
