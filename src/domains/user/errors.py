from dataclasses import dataclass

from domains.__common__.errors import FieldError


@dataclass(eq=False)
class UserEmailValidError(FieldError):
    email: str

    @property
    def message(self) -> str:
        return f"The email '{self.email}' is not valid"


@dataclass(eq=False)
class UserLastNameMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The last name length should not exceed {self.length}"


@dataclass(eq=False)
class UserLastNameMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The last name length should not less than {self.length}"


@dataclass(eq=False)
class UserFirstNameMaxError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The first name length should not exceed {self.length}"


@dataclass(eq=False)
class UserFirstNameMinError(FieldError):
    length: int

    @property
    def message(self) -> str:
        return f"The first name length should not less than {self.length}"
