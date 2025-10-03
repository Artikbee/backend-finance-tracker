from dataclasses import dataclass
from decimal import Decimal
from typing import List

from typing_extensions import Self

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import AccountID, Account


@dataclass(frozen=True, slots=True)
class GetAccountQueryResponse:
    account_id: AccountID
    name: str
    account_type: AccountType
    currency: Currency
    balance: Decimal
    is_active: bool


@dataclass(frozen=True, slots=True)
class GetAccountsQueryResponse:
    accounts: List[GetAccountQueryResponse]

    @classmethod
    def create_model(cls, accounts: List[Account]) -> Self:
        res_accounts = [
            GetAccountQueryResponse(
                account_id=account.oid,
                name=account.name.value,
                account_type=account.account_type,
                currency=account.currency,
                balance=account.balance,
                is_active=account.is_active,
            )
            for account in accounts
        ]
        return cls(accounts=res_accounts)


@dataclass(frozen=True, slots=True)
class GetAccountsQuery:
    access_token: str
