from dataclasses import dataclass

from application.__common__.errors.base_errors import AuthenticationError


@dataclass(eq=False)
class PasswordInvalidError(AuthenticationError):
    @property
    def message(self) -> str:
        return "Invalid password"
