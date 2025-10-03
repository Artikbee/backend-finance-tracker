from dataclasses import dataclass
from decimal import Decimal

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import AccountID
from domains.account.value_objects import AccountName


@dataclass(frozen=True, slots=True)
class CreateAccountCommandResponse:
    account_id: AccountID


@dataclass(frozen=True, slots=True)
class CreateAccountCommand:
    access_token: str
    name: AccountName
    account_type: AccountType
    currency: Currency
    balance: Decimal
