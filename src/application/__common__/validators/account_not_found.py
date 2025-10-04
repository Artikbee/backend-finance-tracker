from application.__common__.errors.account_not_found import AccountNotFoundError
from domains.account.models import Account


def validate_account_not_found(account: Account) -> None:
    if account is None:
        raise AccountNotFoundError()
