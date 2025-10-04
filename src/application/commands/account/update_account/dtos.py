from dataclasses import dataclass
from decimal import Decimal

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import AccountID
from domains.account.value_objects import AccountName


@dataclass(frozen=True, slots=True)
class UpdateAccountCommandResponse:
    account_id: AccountID
    name: str
    account_type: AccountType
    currency: Currency
    balance: Decimal
    is_active: bool


@dataclass(frozen=True, slots=True)
class UpdateAccountCommand:
    access_token: str
    account_id: AccountID
    name: AccountName
    account_type: AccountType
    currency: Currency
    is_active: bool
