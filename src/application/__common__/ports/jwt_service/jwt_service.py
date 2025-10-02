from abc import ABC, abstractmethod
from typing import Tuple, Literal

from domains.user.models import UserID


class JWTService(ABC):
    @abstractmethod
    async def generate(self, user_id: UserID) -> Tuple[str, str]:
        ...

    @abstractmethod
    async def get_expires_time(self) -> Tuple[int, int]:
        ...

    @abstractmethod
    async def verify_and_get_user_id(
            self,
            token: str,
            expected_type: Literal["access", "refresh"] | None = None
    ) -> UserID:
        ...

