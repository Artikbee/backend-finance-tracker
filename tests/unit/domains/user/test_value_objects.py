import pytest

from domains.__common__.base_errors import FieldError
from domains.user.errors import (
    UserEmailValidError,
    UserLastNameMinError,
    UserLastNameMaxError,
)
from domains.user.value_objects import UserEmail, UserLastName


@pytest.mark.value_objects
@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("fake@example.com", None),
        ("fake", UserEmailValidError),
    ]

)
def test_user_email(
        value: str,
        exc_class: type[FieldError] | None,
) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            _ = UserEmail(value)
        assert excinfo.value.message == f"The email '{value}' is not valid"
    else:
        user_email = UserEmail(value)
        assert value == user_email.value
        assert isinstance(user_email, UserEmail)


@pytest.mark.value_objects
@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("", UserLastNameMinError),
        ("f", None),
        ("f" * 50, None),
        ("f" * 51, UserLastNameMaxError),
    ]

)
def test_user_last_name(
        value: str,
        exc_class: type[FieldError] | None,
) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            _ = UserLastName(value)

        user_min_length = 1
        if len(value) < user_min_length:
            msg = "The last name length should not less than 1"
        else:
            msg = "The last name length should not exceed 50"
        assert excinfo.value.message == msg
    else:
        user_last_name = UserLastName(value)
        assert value == user_last_name.value
        assert isinstance(user_last_name, UserLastName)
