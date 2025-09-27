from dataclasses import dataclass
from typing import NewType, cast
from typing_extensions import Self

from domains.__common__.base_entity import BaseEntity
from domains.user.enums import UserRole
from domains.user.value_objects import UserEmail, UserLastName, UserFirstName

UserID = NewType('UserID', int)


@dataclass
class User(BaseEntity[UserID]):
    email: UserEmail
    hashed_password: str
    last_name: UserLastName | None
    first_name: UserFirstName | None
    role: UserRole
    is_active: bool

    def update_email(self, email: UserEmail) -> None:
        self.email = email

    def update_hashed_password(self, hashed_password: str) -> None:
        self.hashed_password = hashed_password

    def update_last_name(self, last_name: UserLastName) -> None:
        self.last_name = last_name

    def update_first_name(self, first_name: UserFirstName) -> None:
        self.first_name = first_name

    def update_role(self, role: UserRole) -> None:
        self.role = role

    def update_is_active(self, is_active: bool) -> None:
        self.is_active = is_active

    @classmethod
    def create(
            cls,
            email: UserEmail,
            hashed_password: str,
            last_name: UserLastName | None,
            first_name: UserFirstName | None,
            role: UserRole,
            is_active: bool,
    ) -> Self:
        return cls(
            oid=cast("UserID", None),
            email=email,
            hashed_password=hashed_password,
            last_name=last_name,
            first_name=first_name,
            role=role,
            is_active=is_active,
        )
