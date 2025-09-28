from application.__common__.errors.user_already_exists import UserAlreadyExistsError
from domains.user.models import User


def validate_user_already_exists(user: User) -> None:
    if user is not None:
        raise UserAlreadyExistsError()
