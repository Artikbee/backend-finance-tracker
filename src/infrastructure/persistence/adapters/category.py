from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.category.gateway import CategoryGateway
from application.__common__.ports.persistence.category.reader import CategoryReader
from domains.account.models import Account, AccountID
from domains.category.models import Category
from domains.user.models import UserID
from infrastructure.persistence.models.account import accounts_table
from infrastructure.persistence.models.category import categories_table


class CategoryReaderAlchemy(CategoryReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_by_user_id(self, user_id: UserID) -> list[Category]:
        stmt = select(Category).where(categories_table.c.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()


class CategoryGatewayAlchemy(CategoryGateway):
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
