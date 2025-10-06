from abc import ABC, abstractmethod

from domains.category.models import Category, CategoryID
from domains.user.models import UserID


class CategoryReader(ABC):
    @abstractmethod
    async def get_all_by_user_id(self, user_id: UserID) -> list[Category]:
        ...

    @abstractmethod
    async def get_by_category_id(self, category_id: CategoryID) -> Category | None:
        ...
