import decimal

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    Table,
    func,
    DECIMAL,
    ForeignKey, Text
)
from sqlalchemy.orm import relationship, composite

from domains.transaction.enums import TransactionType
from domains.transaction.models import Transaction
from domains.transaction.value_objects import TransactionDescription
from infrastructure.persistence.models._base import mapper_registry

transactions_table = Table(
    "transactions",
    mapper_registry.metadata,
    Column(
        "transaction_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "account_id",
        BigInteger,
        ForeignKey("accounts.account_id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "category_id",
        BigInteger,
        ForeignKey("categories.category_id"),
        nullable=False,
    ),
    Column(
        "transaction_type",
        Enum(TransactionType, name="transaction_type"),
        nullable=False,
    ),
    Column(
        "amount",
        DECIMAL,
        nullable=False,
        default=decimal.Decimal("0.00"),
    ),
    Column(
        "description",
        Text,
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


def map_transaction_table() -> None:
    _ = mapper_registry.map_imperatively(
        Transaction,
        transactions_table,
        properties={
            "oid": transactions_table.c.transaction_id,
            "transaction_type": transactions_table.c.transaction_type,
            "amount": transactions_table.c.amount,
            "description": composite(TransactionDescription, transactions_table.c.description),
            "account_id": transactions_table.c.account_id,
            "category_id": transactions_table.c.category_id,
            "account": relationship(
                "Account",
                back_populates="transactions",
            ),
            "category": relationship(
                "Category",
                back_populates="transactions",
            ),
        },
        column_prefix="_",
    )
