import pytest

from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import (
    UserEmail,
    UserFirstName,
    UserLastName,
)


@pytest.fixture(scope="module")
def user() -> User:
    return User.create(
        email=UserEmail("test@example.com"),
        hashed_password="hashed_pwd",
        last_name=UserLastName("Doe"),
        first_name=UserFirstName("John"),
        role=UserRole.USER,
        is_active=True,
    )
