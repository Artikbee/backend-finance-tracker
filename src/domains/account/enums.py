from enum import Enum


class AccountType(str, Enum):
    CASH = 'cash'
    CRYPTO = 'crypto'
    BANK = 'bank'
    CREDIT_CARD = 'credit_card'
