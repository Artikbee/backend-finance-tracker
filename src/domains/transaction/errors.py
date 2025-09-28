from dataclasses import dataclass

from domains.__common__.base_errors import FieldError


@dataclass(eq=False)
class TransactionDescriptionMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The description length should not exceed {self.length}"


@dataclass(eq=False)
class TransactionDescriptionMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The description length should not less than {self.length}"
