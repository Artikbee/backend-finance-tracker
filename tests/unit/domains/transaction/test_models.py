from decimal import Decimal

import pytest

from domains.account.models import AccountID
from domains.category.models import CategoryID
from domains.transaction.enums import TransactionType
from domains.transaction.models import Transaction
from domains.transaction.value_objects import TransactionDescription


@pytest.mark.models
def test_create_transaction(transaction: Transaction) -> None:
    assert isinstance(transaction, Transaction)
    assert transaction.account_id == AccountID(1)
    assert transaction.category_id == CategoryID(1)
    assert transaction.transaction_type == TransactionType.INCOME
    assert transaction.amount == Decimal(10)
    assert transaction.description == TransactionDescription("123")
