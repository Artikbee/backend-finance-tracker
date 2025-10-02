from application.__common__.errors.password_invalid import PasswordInvalidError


def validate_password_invalid(is_correct_password: bool) -> None:
    if not is_correct_password:
        raise PasswordInvalidError()
