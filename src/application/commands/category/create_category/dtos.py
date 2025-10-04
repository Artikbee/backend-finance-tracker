from dataclasses import dataclass

from domains.category.models import CategoryID
from domains.category.value_objects import CategoryName


@dataclass(frozen=True, slots=True)
class CreateCategoryCommandResponse:
    category_id: CategoryID


@dataclass(frozen=True, slots=True)
class CreateCategoryCommand:
    access_token: str
    name: CategoryName
