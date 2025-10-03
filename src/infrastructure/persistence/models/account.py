import decimal

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    String,
    Table,
    func,
    Boolean,
    DECIMAL,
    ForeignKey
)
from sqlalchemy.orm import relationship, composite

from domains.__common__.enums import Currency
from domains.account.enums import AccountType
from domains.account.models import Account
from domains.account.value_objects import AccountName
from infrastructure.persistence.models._base import mapper_registry

accounts_table = Table(
    "accounts",
    mapper_registry.metadata,
    Column(
        "account_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "user_id",
        BigInteger,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "name",
        String,
        nullable=False,
    ),
    Column(
        "account_type",
        Enum(AccountType, name="account_type"),
        nullable=False,
    ),
    Column(
        "currency",
        Enum(Currency, name="currency"),
        nullable=False,
    ),
    Column(
        "balance",
        DECIMAL,
        nullable=False,
        default=decimal.Decimal("0.00"),
    ),
    Column(
        "is_active",
        Boolean,
        nullable=False,
    ),
    Column(
        "created_at",
        DateTime,
        default=func.now(),
        server_default=func.now(),
        nullable=False,
    ),
    Column(
        "updated_at",
        DateTime,
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        server_onupdate=func.now(),
        nullable=True,
    ),
)


def map_account_table() -> None:
    _ = mapper_registry.map_imperatively(
        Account,
        accounts_table,
        properties={
            "oid": accounts_table.c.account_id,
            "name": composite(AccountName, accounts_table.c.name),
            "account_type": accounts_table.c.account_type,
            "currency": accounts_table.c.currency,
            "balance": accounts_table.c.balance,
            "is_active": accounts_table.c.is_active,
            "user_id": accounts_table.c.user_id,
            "user": relationship(
                "User",
                back_populates="accounts",
            ),
        },
        column_prefix="_",
    )
