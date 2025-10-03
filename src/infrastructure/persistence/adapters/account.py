from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.account.reader import AccountReader
from domains.account.models import Account
from domains.user.models import UserID
from infrastructure.persistence.models.account import accounts_table


class AccountReaderAlchemy(AccountReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_by_user_id(self, user_id: UserID) -> list[Account]:
        stmt = select(Account).where(accounts_table.c.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()


class AccountGatewayAlchemy(AccountGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
