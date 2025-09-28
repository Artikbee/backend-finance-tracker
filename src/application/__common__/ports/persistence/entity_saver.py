from abc import ABC, abstractmethod

from domains.__common__.base_entity import BaseEntity, OIDType


class EntitySaver(ABC):
    @abstractmethod
    def add_one(self, entity: BaseEntity[OIDType]) -> None: ...

    @abstractmethod
    async def delete(self, entity: BaseEntity[OIDType]) -> None: ...
