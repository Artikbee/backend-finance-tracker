from dataclasses import dataclass

from domains.user.value_objects import UserEmail


@dataclass(frozen=True, slots=True)
class RegisterUserCommandResponse:
    message: str


@dataclass(frozen=True, slots=True)
class RegisterUserCommand:
    email: UserEmail
    password: str
