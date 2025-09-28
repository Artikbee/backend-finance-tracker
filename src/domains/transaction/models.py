from dataclasses import dataclass
from decimal import Decimal
from typing import NewType, cast

from typing_extensions import Self

from domains.__common__.base_entity import BaseEntity
from domains.account.models import AccountID
from domains.category.models import CategoryID
from domains.transaction.enums import TransactionType
from domains.transaction.value_objects import TransactionDescription

TransactionID = NewType("TransactionID", int)


@dataclass(slots=True, kw_only=True)
class Transaction(BaseEntity[TransactionID]):
    account_id: AccountID
    category_id: CategoryID
    transaction_type: TransactionType
    amount: Decimal
    description: TransactionDescription

    @classmethod
    def create(
            cls,
            account_id: AccountID,
            category_id: CategoryID,
            transaction_type: TransactionType,
            amount: Decimal,
            description: TransactionDescription,
    ) -> Self:
        return cls(
            oid=cast("TransactionID", None),
            account_id=account_id,
            category_id=category_id,
            transaction_type=transaction_type,
            amount=amount,
            description=description,
        )
