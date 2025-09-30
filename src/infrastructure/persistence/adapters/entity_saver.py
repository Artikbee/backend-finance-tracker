from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.persistence.entity_saver import EntitySaver
from domains.__common__.base_entity import BaseEntity, OIDType


class EntitySaverAlchemy(EntitySaver):
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    def add_one(self, entity: BaseEntity[OIDType]) -> None:
        self._session.add(entity)

    async def delete(self, entity: BaseEntity[OIDType]) -> None:
        await self._session.delete(entity)
