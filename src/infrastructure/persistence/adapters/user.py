from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.ports.persistence.user.reader import UserReader
from domains.user.models import User, UserID
from domains.user.value_objects import UserEmail


class UserReaderAlchemy(UserReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session


class UserGatewayAlchemy(UserGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_email_and_password(
            self,
            email: UserEmail,
            hashed_password: str,
    ) -> User | None:
        ...

    async def get_by_email(self, email: UserEmail) -> User | None:
        ...

    async def get_by_user_id(self, user_id: UserID) -> User | None:
        ...
