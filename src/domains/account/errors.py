from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass
class AccountNameMaxError(FieldError):
    length: int

    def message(self) -> str:
        return f"The account name length should not exceed {self.length}"


@dataclass
class AccountNameMinError(FieldError):
    length: int

    def message(self) -> str:
        return f"The account name length should not less than {self.length}"


@dataclass
class AccountCurrencyAvailableError(FieldError):
    currency: str

    def message(self) -> str:
        return f"The account currency '{self.currency}' is not available"
