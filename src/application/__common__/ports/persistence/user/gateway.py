from abc import ABC, abstractmethod

from domains.user.models import User
from domains.user.value_objects import UserEmail


class UserGateway(ABC):
    @abstractmethod
    async def get_by_email(self, email: UserEmail) -> User | None:
        ...
