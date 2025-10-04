from abc import ABC, abstractmethod

from domains.account.models import AccountID, Account
from domains.user.models import UserID


class CategoryGateway(ABC):
    @abstractmethod
    async def get_by_account_id_and_user_id(
            self,
            user_id: UserID,
            account_id: AccountID,
    ) -> Account | None:
        ...
