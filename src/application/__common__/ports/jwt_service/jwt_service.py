from abc import ABC, abstractmethod
from typing import Tuple

from domains.user.models import UserID


class JWTService(ABC):
    @abstractmethod
    async def generate(self, user_id: UserID) -> Tuple[str, str]:
        ...

    @abstractmethod
    async def get_expires_time(self) -> Tuple[int, int]:
        ...
