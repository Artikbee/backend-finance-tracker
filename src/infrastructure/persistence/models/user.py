from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    String,
    Table,
    func,
    Boolean,
)
from sqlalchemy.orm import composite, relationship

from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import UserEmail, UserLastName, UserFirstName
from infrastructure.persistence.models._base import mapper_registry

users_table = Table(
    "users",
    mapper_registry.metadata,
    Column(
        "user_id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "email",
        String,
        nullable=False,
    ),
    Column(
        "hashed_password",
        String,
        nullable=False,
    ),
    Column(
        "last_name",
        String,
        nullable=True,
    ),
    Column(
        "first_name",
        String,
        nullable=True,
    ),
    Column(
        "role",
        Enum(UserRole, name="user_role"),
        nullable=False,
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


def map_user_table() -> None:
    _ = mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "oid": users_table.c.user_id,
            "email": composite(UserEmail, users_table.c.email),
            "hashed_password": users_table.c.hashed_password,
            "last_name": composite(UserLastName, users_table.c.last_name),
            "first_name": composite(UserFirstName, users_table.c.first_name),
            "is_active": users_table.c.is_active,
            "role": users_table.c.role,
            "accounts": relationship(
                "Account",
                back_populates="user",
                cascade="all, delete-orphan",
            ),
            "categories": relationship(
                "Category",
                back_populates="user",
                cascade="all, delete-orphan",
            ),
        },
        column_prefix="_",
    )
