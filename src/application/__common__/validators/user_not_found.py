from application.__common__.errors.user_not_found import UserNotFoundError
from domains.user.models import User


def validate_user_not_found(user: User) -> None:
    if user is None:
        raise UserNotFoundError()
