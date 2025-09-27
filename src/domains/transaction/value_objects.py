from dataclasses import dataclass

from domains.__common__.constants import CURRENCIES
from domains.transaction.errors import (
    TransactionCurrencyAvailableError,
    TransactionDescriptionMaxError,
    TransactionDescriptionMinError,
)


@dataclass(slots=True, frozen=True, eq=True)
class TransactionCurrency:
    value: str

    def __post_init__(self) -> None:
        if self.value not in CURRENCIES:
            raise TransactionCurrencyAvailableError(self.value)


@dataclass(slots=True, frozen=True, eq=True)
class TransactionDescription:
    value: str

    def __post_init__(self) -> None:
        description_min_length = 1
        description_max_length = 100
        if len(self.value) < description_min_length:
            raise TransactionDescriptionMinError(description_min_length)
        if len(self.value) > description_max_length:
            raise TransactionDescriptionMaxError(description_max_length)
