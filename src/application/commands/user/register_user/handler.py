import logging

from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.validators.user_already_exists import validate_user_already_exists
from application.commands.user.register_user.dtos import RegisterUserCommand, RegisterUserCommandResponse
from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import UserEmail

logger = logging.getLogger(__name__)


class RegisterUserCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver

    async def run(self, data: RegisterUserCommand) -> RegisterUserCommandResponse:
        user = await self._user_gateway.get_by_email(email=UserEmail(data.email))
        validate_user_already_exists(user)

        user = User.create(
            email=UserEmail(data.email),
            hashed_password=data.password,
            last_name=None,
            first_name=None,
            role=UserRole.USER,
            is_active=True,
        )
        self._entity_saver.add_one(user)
        await self._transaction_db.commit()

        return RegisterUserCommandResponse(
            message="Check your email",
        )
