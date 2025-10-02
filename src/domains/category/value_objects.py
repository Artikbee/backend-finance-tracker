from dataclasses import dataclass

from domains.category.errors import CategoryNameMinError, CategoryNameMaxError


@dataclass(slots=True, frozen=True, eq=True)
class CategoryName:
    value: str | None

    def __post_init__(self) -> None:
        if self.value is None:
            return
        name_min_length = 1
        name_max_length = 100
        if len(self.value) < name_min_length:
            raise CategoryNameMinError(name_min_length)
        if len(self.value) > name_max_length:
            raise CategoryNameMaxError(name_max_length)
