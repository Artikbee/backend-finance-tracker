from decimal import Decimal

from pydantic import BaseModel

from domains.__common__.enums import Currency
from domains.account.enums import AccountType


class CreateAccountSchema(BaseModel):
    name: str
    account_type: AccountType
    currency: Currency
    balance: Decimal


class UpdateAccountSchema(BaseModel):
    name: str
    account_type: AccountType
    currency: Currency
    is_active: bool