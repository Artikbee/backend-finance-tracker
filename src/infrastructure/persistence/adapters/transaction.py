from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.transaction.reader import TransactionReader
from domains.account.models import AccountID
from domains.transaction.models import Transaction
from infrastructure.persistence.models.transaction import transactions_table


class TransactionReaderAlchemy(TransactionReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_by_account_id(self, account_id: AccountID) -> list[Transaction]:
        stmt = select(Transaction).where(transactions_table.c.account_id == account_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()
