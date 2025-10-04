from dataclasses import dataclass

from application.__common__.errors.base_errors import NotFoundError


@dataclass(eq=False)
class AccountNotFoundError(NotFoundError):
    @property
    def message(self) -> str:
        return "Account not found"
