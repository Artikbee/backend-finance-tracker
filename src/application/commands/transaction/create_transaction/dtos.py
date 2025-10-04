from dataclasses import dataclass
from decimal import Decimal

from domains.account.models import AccountID
from domains.category.models import CategoryID
from domains.transaction.enums import TransactionType
from domains.transaction.models import TransactionID
from domains.transaction.value_objects import TransactionDescription


@dataclass(frozen=True, slots=True)
class CreateTransactionCommandResponse:
    transaction_id: TransactionID


@dataclass(frozen=True, slots=True)
class CreateTransactionCommand:
    access_token: str
    account_id: AccountID
    category_id: CategoryID
    transaction_type: TransactionType
    amount: Decimal
    description: TransactionDescription
