from abc import ABC, abstractmethod

from domains.account.models import Account
from domains.user.models import UserID


class AccountReader(ABC):
    @abstractmethod
    async def get_all_by_user_id(self, user_id: UserID) -> list[Account]:
        ...
