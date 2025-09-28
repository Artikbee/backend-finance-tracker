from dataclasses import dataclass

from domains.transaction.errors import (
    TransactionDescriptionMaxError,
    TransactionDescriptionMinError,
)


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
