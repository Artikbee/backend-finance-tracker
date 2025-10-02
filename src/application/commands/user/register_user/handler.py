import logging

from application.__common__.ports.password_hasher_service.password_hasher_service import PasswordHasherService
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.validators.user_already_exists import validate_user_already_exists
from application.commands.user.register_user.dtos import RegisterUserCommand, RegisterUserCommandResponse
from domains.user.enums import UserRole
from domains.user.models import User

logger = logging.getLogger(__name__)


class RegisterUserCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
            password_hasher_service: PasswordHasherService,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver
        self._password_hasher_service = password_hasher_service

    async def run(self, data: RegisterUserCommand) -> RegisterUserCommandResponse:
        user = await self._user_gateway.get_by_email(email=data.email)
        validate_user_already_exists(user)

        hashed_password = self._password_hasher_service.hash_password(data.password)

        new_user = User.create(
            email=data.email,
            hashed_password=hashed_password,
            last_name=None,
            first_name=None,
            role=UserRole.USER,
            is_active=True,
        )
        self._entity_saver.add_one(new_user)
        await self._transaction_db.commit()

        return RegisterUserCommandResponse(
            message=f"Check your email",
        )
