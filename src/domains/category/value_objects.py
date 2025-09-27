from dataclasses import dataclass

from domains.category.errors import CategoryNameMinError, CategoryNameMaxError


@dataclass
class CategoryName:
    value: str

    def __post_init__(self) -> None:
        name_min_length = 1
        name_max_length = 100
        if len(self.value) < name_min_length:
            raise CategoryNameMinError(name_min_length)
        if len(self.value) > name_max_length:
            raise CategoryNameMaxError(name_max_length)
