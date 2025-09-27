from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass
class TransactionCurrencyAvailableError(FieldError):
    currency: str

    def message(self) -> str:
        return f"The currency '{self.currency}' is not available"


@dataclass
class TransactionDescriptionMaxError(FieldError):
    length: int

    def message(self) -> str:
        return f"The description length should not exceed {self.length}"


@dataclass
class TransactionDescriptionMinError(FieldError):
    length: int

    def message(self) -> str:
        return f"The description length should not less than {self.length}"
