from abc import ABC, abstractmethod

from domains.user.models import UserID, User


class UserReader(ABC):
    @abstractmethod
    async def get_by_user_id(self, user_id: UserID) -> User | None:
        ...
