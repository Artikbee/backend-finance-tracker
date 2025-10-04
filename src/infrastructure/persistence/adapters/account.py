from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.account.reader import AccountReader
from domains.account.models import Account, AccountID
from domains.user.models import UserID
from infrastructure.persistence.models.account import accounts_table


class AccountReaderAlchemy(AccountReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_by_user_id(self, user_id: UserID) -> list[Account]:
        stmt = select(Account).where(accounts_table.c.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_by_account_id_and_user_id(
            self,
            user_id: UserID,
            account_id: AccountID,
    ) -> Account | None:
        stmt = select(Account).where(
            and_(
                accounts_table.c.user_id == user_id,
                accounts_table.c.account_id == account_id,
            )

        )
        result = await self._session.execute(stmt)
        return result.one_or_none()


class AccountGatewayAlchemy(AccountGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_account_id_and_user_id(
            self,
            user_id: UserID,
            account_id: AccountID,
    ) -> Account | None:
        stmt = select(Account).where(
            and_(
                accounts_table.c.user_id == user_id,
                accounts_table.c.account_id == account_id,
            )

        )
        result = await self._session.execute(stmt)
        return result.scalars().one_or_none()
