from abc import ABC, abstractmethod

from domains.user.models import User, UserID
from domains.user.value_objects import UserEmail


class UserGateway(ABC):
    @abstractmethod
    async def get_by_email_and_password(
            self,
            email: UserEmail,
            hashed_password: str,
    ) -> User | None:
        ...

    @abstractmethod
    async def get_by_email(self, email: UserEmail) -> User | None:
        ...

    @abstractmethod
    async def get_by_user_id(self, user_id: UserID) -> User | None:
        ...
