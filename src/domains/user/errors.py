from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass
class UserEmailValidError(FieldError):
    email: str

    @property
    def message(self) -> str:
        return f"The email '{self.email}' is not valid"


@dataclass
class UserLastNameMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The last name length should not exceed {self.length}"


@dataclass
class UserLastNameMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The last name length should not less than {self.length}"


@dataclass
class UserFirstNameMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The first name length should not exceed {self.length}"


@dataclass
class UserFirstNameMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The first name length should not less than {self.length}"
