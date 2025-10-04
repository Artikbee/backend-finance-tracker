from dataclasses import dataclass
from decimal import Decimal

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import AccountID


@dataclass(frozen=True, slots=True)
class GetAccountQueryResponse:
    account_id: int
    name: str
    account_type: AccountType
    currency: Currency
    balance: Decimal
    is_active: bool


@dataclass(frozen=True, slots=True)
class GetAccountQuery:
    access_token: str
    account_id: AccountID
