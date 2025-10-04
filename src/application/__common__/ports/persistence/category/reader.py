from abc import ABC, abstractmethod

from domains.category.models import Category
from domains.user.models import UserID


class CategoryReader(ABC):
    @abstractmethod
    async def get_all_by_user_id(self, user_id: UserID) -> list[Category]:
        ...
