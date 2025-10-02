from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from application.__common__.ports.password_hasher_service.password_hasher_service import PasswordHasherService


class PasswordHasherServiceAdapter(PasswordHasherService):
    def __init__(self) -> None:
        self._ph = PasswordHasher()

    def hash_password(self, password: str) -> str:
        return self._ph.hash(password)

    def verify_password(
            self,
            hashed: str,
            password: str
    ) -> bool:
        try:
            return self._ph.verify(hashed, password)
        except VerifyMismatchError:
            return False
