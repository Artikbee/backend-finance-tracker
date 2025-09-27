import re
from dataclasses import dataclass

from domains.user.errors import (
    UserEmailValidError,
    UserLastNameMinError,
    UserLastNameMaxError,
    UserFirstNameMinError,
    UserFirstNameMaxError,
)


@dataclass(slots=True, frozen=True, eq=True)
class UserEmail:
    value: str

    def __post_init__(self) -> None:
        pattern = r'[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, self.value):
            raise UserEmailValidError(email=self.value)


@dataclass(slots=True, frozen=True, eq=True)
class UserLastName:
    value: str

    def __post_init__(self) -> None:
        last_name_min_length = 1
        last_name_max_length = 50
        if len(self.value) < last_name_min_length:
            raise UserLastNameMinError(last_name_min_length)
        if len(self.value) > last_name_max_length:
            raise UserLastNameMaxError(last_name_max_length)


@dataclass(slots=True, frozen=True, eq=True)
class UserFirstName:
    value: str

    def __post_init__(self) -> None:
        first_name_min_length = 1
        first_name_max_length = 50
        if len(self.value) < first_name_min_length:
            raise UserFirstNameMinError(first_name_min_length)
        if len(self.value) > first_name_max_length:
            raise UserFirstNameMaxError(first_name_max_length)
