from abc import ABC, abstractmethod

from domains.account.models import Account, AccountID
from domains.user.models import UserID


class AccountReader(ABC):
    @abstractmethod
    async def get_all_by_user_id(self, user_id: UserID) -> list[Account]:
        ...

    @abstractmethod
    async def get_by_account_id_and_user_id(
            self,
            user_id: UserID,
            account_id: AccountID,
    ) -> Account | None:
        ...
