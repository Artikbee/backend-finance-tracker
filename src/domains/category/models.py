from dataclasses import dataclass
from typing import NewType, cast
from typing_extensions import Self

from domains.__common__.base_entity import BaseEntity
from domains.user.models import UserID

CategoryID = NewType('CategoryID', int)


@dataclass
class Category(BaseEntity[CategoryID]):
    user_id: UserID
    name: str

    def update_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def create(
            cls,
            user_id: UserID,
            name: str
    ) -> Self:
        return cls(
            oid=cast("CategoryID", None),
            user_id=user_id,
            name=name
        )
