from enum import Enum


class AccountType(str, Enum):
    CASH = 'cash'
    CARD = 'card'
