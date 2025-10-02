from dataclasses import dataclass

from domains.user.models import UserID
from domains.user.value_objects import UserLastName, UserFirstName


@dataclass(frozen=True, slots=True)
class UpdateUserCommandResponse:
    user_id: UserID
    last_name: str
    first_name: str
    is_active: bool


@dataclass(frozen=True, slots=True)
class UpdateUserCommand:
    access_token: str
    last_name: UserLastName
    first_name: UserFirstName
    is_active: bool
