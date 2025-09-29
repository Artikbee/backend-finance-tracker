import logging

from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.commands.user.update_user.dtos import (
    UpdateUserCommand,
    UpdateUserCommandResponse,
)

logger = logging.getLogger(__name__)


class UpdateUserCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver

    async def run(self, data: UpdateUserCommand) -> UpdateUserCommandResponse:
        user = await self._user_gateway.get_by_user_id(user_id=data.user_id)

        user.update_is_active(data.is_active)
        user.update_last_name(data.last_name)
        user.update_first_name(data.first_name)

        await self._transaction_db.flush()

        return UpdateUserCommandResponse(
            user_id=user.oid,
            last_name=user.last_name,
            first_name=user.first_name,
            is_active=user.is_active,
        )
