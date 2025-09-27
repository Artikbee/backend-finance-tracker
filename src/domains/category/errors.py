from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass(eq=False)
class CategoryNameMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The category name length should not exceed {self.length}"


@dataclass(eq=False)
class CategoryNameMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The category name length should not less than {self.length}"
