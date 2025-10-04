from dataclasses import dataclass

from domains.account.models import AccountID


@dataclass(frozen=True, slots=True)
class DeleteAccountCommand:
    access_token: str
    account_id: AccountID
