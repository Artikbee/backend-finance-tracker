from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass
class CategoryNameMaxError(FieldError):
    length: int

    def message(self) -> str:
        return f"The category name length should not exceed {self.length}"


@dataclass
class CategoryNameMinError(FieldError):
    length: int

    def message(self) -> str:
        return f"The category name length should not less than {self.length}"
