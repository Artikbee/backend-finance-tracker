import pytest

from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import (
    UserEmail,
    UserFirstName,
    UserLastName,
)


@pytest.mark.models
def test_create_user(user: User) -> None:
    assert user.oid is None
    assert user.email == UserEmail("test@example.com")
    assert user.hashed_password == "hashed_pwd"
    assert user.last_name == UserLastName("Doe")
    assert user.first_name == UserFirstName("John")
    assert user.role == UserRole.USER
    assert user.is_active is True


@pytest.mark.models
def test_update_email(user: User) -> None:
    user.update_email(UserEmail("new@example.com"))
    assert user.email == UserEmail("new@example.com")


@pytest.mark.models
def test_update_hashed_password(user: User) -> None:
    user.update_hashed_password("new_hashed")
    assert user.hashed_password == "new_hashed"


@pytest.mark.models
def test_update_last_name(user: User) -> None:
    user.update_last_name(UserLastName("Smith"))
    assert user.last_name == UserLastName("Smith")


@pytest.mark.models
def test_update_first_name(user: User) -> None:
    user.update_first_name(UserFirstName("Alice"))
    assert user.first_name == UserFirstName("Alice")


@pytest.mark.models
def test_update_role(user: User) -> None:
    user.update_role(UserRole.ADMIN)
    assert user.role == UserRole.ADMIN


@pytest.mark.models
def test_update_is_active(user: User) -> None:
    user.update_is_active(False)
    assert user.is_active is False
