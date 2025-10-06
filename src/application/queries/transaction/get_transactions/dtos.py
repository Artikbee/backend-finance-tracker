from dataclasses import dataclass
from decimal import Decimal
from typing import List

from domains.account.models import AccountID
from domains.transaction.enums import TransactionType


@dataclass(frozen=True, slots=True)
class GetTransactionQueryResponse:
    category_name: str
    transaction_type: TransactionType
    amount: Decimal
    description: str


@dataclass(frozen=True, slots=True)
class GetTransactionsQueryResponse:
    transactions: List[GetTransactionQueryResponse]


@dataclass(frozen=True, slots=True)
class GetTransactionsQuery:
    access_token: str
    account_id: AccountID
