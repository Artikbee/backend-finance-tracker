import re
from dataclasses import dataclass

from src.domains.user.errors import UserEmailNotValid


@dataclass
class UserEmail:
    value: str

    def __post_init__(self) -> None:
        pattern = r'[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, self.value):
            raise UserEmailNotValid(email=self.value)


@dataclass
class UserLastName:
    value: str

    def __post_init__(self) -> None:
        ...


@dataclass
class UserFirstName:
    value: str

    def __post_init__(self) -> None:
        ...
