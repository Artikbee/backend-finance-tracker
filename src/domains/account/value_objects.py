from dataclasses import dataclass

from domains.__common__.constants import CURRENCIES
from domains.account.errors import AccountNameMinError, AccountNameMaxError, AccountCurrencyAvailableError


@dataclass(slots=True, frozen=True, eq=True)
class AccountName:
    value: str

    def __post_init__(self) -> None:
        name_min_length = 1
        name_max_length = 50
        if len(self.value) < name_min_length:
            raise AccountNameMinError(name_min_length)
        if len(self.value) > name_max_length:
            raise AccountNameMaxError(name_max_length)


@dataclass(slots=True, frozen=True, eq=True)
class AccountCurrency:
    value: str

    def __post_init__(self) -> None:
        if self.value not in CURRENCIES:
            raise AccountCurrencyAvailableError(self.value)
