from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.ports.persistence.user.reader import UserReader
from domains.user.models import User, UserID
from domains.user.value_objects import UserEmail
from infrastructure.persistence.models.user import users_table


class UserReaderAlchemy(UserReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_user_id(self, user_id: UserID) -> User | None:
        stmt = select(User).where(users_table.c.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()


class UserGatewayAlchemy(UserGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_email_and_password(
            self,
            email: UserEmail,
            hashed_password: str,
    ) -> User | None:
        stmt = select(User).where(
            and_(
                users_table.c.email == email.value,
                users_table.c.hashed_password == hashed_password,
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: UserEmail) -> User | None:
        stmt = select(User).where(users_table.c.email == email.value)
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: UserID) -> User | None:
        stmt = select(User).where(users_table.c.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()
