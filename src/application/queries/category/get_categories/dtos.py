from dataclasses import dataclass
from typing import List

from typing_extensions import Self

from domains.category.models import CategoryID, Category


@dataclass(frozen=True, slots=True)
class GetCategoryQueryResponse:
    category_id: CategoryID
    name: str


@dataclass(frozen=True, slots=True)
class GetCategoriesQueryResponse:
    categories: List[GetCategoryQueryResponse]

    @classmethod
    def create_model(cls, categories: List[Category]) -> Self:
        res_categories = [
            GetCategoryQueryResponse(
                category_id=category.oid,
                name=category.name.value,
            )
            for category in categories
        ]
        return cls(categories=res_categories)


@dataclass(frozen=True, slots=True)
class GetCategoriesQuery:
    access_token: str
