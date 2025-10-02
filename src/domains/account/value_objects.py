from dataclasses import dataclass

from domains.account.errors import AccountNameMinError, AccountNameMaxError


@dataclass(slots=True, frozen=True, eq=True)
class AccountName:
    value: str | None

    def __post_init__(self) -> None:
        if self.value is None:
            return
        name_min_length = 1
        name_max_length = 50
        if len(self.value) < name_min_length:
            raise AccountNameMinError(name_min_length)
        if len(self.value) > name_max_length:
            raise AccountNameMaxError(name_max_length)
