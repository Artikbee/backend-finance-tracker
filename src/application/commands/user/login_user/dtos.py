from dataclasses import dataclass

from domains.user.value_objects import UserEmail


@dataclass(frozen=True, slots=True)
class LoginUserCommandResponse:
    access_token: str
    access_expires_in: int
    refresh_token: str
    refresh_expires_in: int
    token_type: str


@dataclass(frozen=True, slots=True)
class LoginUserCommand:
    email: UserEmail
    password: str
