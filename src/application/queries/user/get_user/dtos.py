from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GetUserCommandResponse:
    email: str
    last_name: str
    first_name: str
    role: str
    is_active: bool


@dataclass(frozen=True, slots=True)
class GetUserCommand:
    access_token: str
