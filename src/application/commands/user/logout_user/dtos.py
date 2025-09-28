from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LogoutUserCommandResponse:
    message: str


@dataclass(frozen=True, slots=True)
class LogoutUserCommand:
    refresh_token: str
