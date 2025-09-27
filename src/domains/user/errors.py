from dataclasses import dataclass

from src.domains.__common__.errors import FieldError


@dataclass
class UserEmailNotValid(FieldError):
    email: str

    def message(self) -> str:
        return f"The email '{self.email}' is not valid"
