from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DeleteUserCommand:
    access_token: str
    user_id: int
