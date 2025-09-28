from dataclasses import dataclass

from domains.__common__.base_errors import FieldError


@dataclass(eq=False)
class AccountNameMaxError(FieldError):
    length: int

    def message(self) -> str:
        return f"The account name length should not exceed {self.length}"


@dataclass(eq=False)
class AccountNameMinError(FieldError):
    length: int

    def message(self) -> str:
        return f"The account name length should not less than {self.length}"
