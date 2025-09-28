from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RegisterUserCommandResponse:
    message: str


@dataclass(frozen=True, slots=True)
class RegisterUserCommand:
    email: str
    password: str
