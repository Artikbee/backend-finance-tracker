from abc import ABC, abstractmethod

from domains.account.models import AccountID
from domains.transaction.models import Transaction


class TransactionReader(ABC):
    @abstractmethod
    async def get_all_by_account_id(self, account_id: AccountID) -> list[Transaction]:
        ...
