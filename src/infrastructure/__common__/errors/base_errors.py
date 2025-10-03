from dataclasses import dataclass


@dataclass(eq=False)
class InfrastructureError(Exception):
    @property
    def message(self) -> str:
        return "Infrastructure error occurred"
