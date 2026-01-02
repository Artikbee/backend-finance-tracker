from decimal import Decimal

import pytest

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import Account
from domains.account.value_objects import AccountName
from domains.user.models import UserID


@pytest.fixture(scope="module")
def account() -> Account:
    return Account.create(
        user_id=UserID(1),
        name=AccountName("Account Name"),
        account_type=AccountType.CARD,
        currency=Currency.EUR,
        balance=Decimal(10),
        is_active=True,
    )
