from abc import ABC, abstractmethod


class PasswordHasherService(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        ...

    @abstractmethod
    def verify_password(
            self,
            hashed: str,
            password: str
    ) -> bool:
        ...
