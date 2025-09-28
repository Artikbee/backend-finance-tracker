import decimal
from dataclasses import dataclass
from typing import NewType, cast

from typing_extensions import Self

from domains.__common__.base_entity import BaseEntity
from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.value_objects import AccountName
from domains.user.models import UserID

AccountID = NewType('AccountID', int)


@dataclass(slots=True)
class Account(BaseEntity[AccountID]):
    user_id: UserID
    name: AccountName
    account_type: AccountType
    currency: Currency
    balance: decimal.Decimal
    is_active: bool

    def update_name(self, name: AccountName) -> None:
        self.name = name

    def update_type(self, account_type: AccountType) -> None:
        self.account_type = account_type

    def update_currency(self, currency: Currency) -> None:
        self.currency = currency

    def update_balance(self, balance: decimal.Decimal) -> None:
        self.balance = balance

    def update_is_active(self, is_active: bool) -> None:
        self.is_active = is_active

    @classmethod
    def create(
            cls,
            user_id: UserID,
            name: AccountName,
            account_type: AccountType,
            currency: Currency,
            balance: decimal.Decimal,
            is_active: bool,
    ) -> Self:
        return cls(
            oid=cast(AccountID, None),
            user_id=user_id,
            name=name,
            account_type=account_type,
            currency=currency,
            balance=balance,
            is_active=is_active,
        )
