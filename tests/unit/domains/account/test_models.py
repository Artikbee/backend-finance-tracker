from decimal import Decimal

import pytest

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import Account
from domains.account.value_objects import AccountName
from domains.user.models import UserID


@pytest.fixture
def account() -> Account:
    return Account.create(
        user_id=UserID(1),
        name=AccountName("Account Name"),
        account_type=AccountType.CARD,
        currency=Currency.EUR,
        balance=Decimal(10),
        is_active=True,
    )


def test_create_account(account: Account) -> None:
    assert isinstance(account, Account)
    assert account.user_id == UserID(1)
    assert account.name == AccountName("Account Name")
    assert account.account_type == AccountType.CARD
    assert account.currency == Currency.EUR
    assert account.balance == Decimal(10)
    assert account.is_active == True
    assert account.oid is None


def test_update_name(account: Account) -> None:
    account.update_name(AccountName("Account Name1"))
    assert account.name == AccountName("Account Name1")


def test_update_account_type(account: Account) -> None:
    account.update_account_type(AccountType.CASH)
    assert account.account_type == AccountType.CASH


def test_update_currency(account: Account) -> None:
    account.update_currency(Currency.USD)
    assert account.currency == Currency.USD


def test_update_balance(account: Account) -> None:
    account.update_balance(Decimal(15))
    assert account.balance == Decimal(15)


def test_update_is_active(account: Account) -> None:
    account.update_is_active(False)
    assert account.is_active == False
