from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    String,
    Table,
    func,
    ForeignKey
)
from sqlalchemy.orm import relationship, composite

from domains.category.models import Category
from domains.category.value_objects import CategoryName
from infrastructure.persistence.models._base import mapper_registry

categories_table = Table(
    "categories",
    mapper_registry.metadata,
    Column(
        "category_id",
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


def map_category_table() -> None:
    _ = mapper_registry.map_imperatively(
        Category,
        categories_table,
        properties={
            "oid": categories_table.c.category_id,
            "name": composite(CategoryName, categories_table.c.name),
            "user_id": categories_table.c.user_id,
            "user": relationship(
                "User",
                back_populates="categories",
            ),
            "transactions": relationship(
                "Transaction",
                back_populates="category",
            )
        },
        column_prefix="_",
    )
