from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.transaction_db import TransactionDB


class TransactionDBAlchemy(TransactionDB):
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def commit(self) -> None:
        await self._session.commit()

    async def flush(self) -> None:
        await self._session.flush()
