from dataclasses import dataclass

from infrastructure.__common__.errors.base_errors import InfrastructureError


@dataclass(eq=False)
class JWTError(InfrastructureError):
    @property
    def message(self) -> str:
        return "Invalid JWT token"
