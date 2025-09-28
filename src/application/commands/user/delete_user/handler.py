import logging

from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.commands.user.delete_user.dtos import DeleteUserCommand
from domains.user.models import UserID

logger = logging.getLogger(__name__)


class DeleteUserCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver

    async def run(self, data: DeleteUserCommand) -> None:
        user = await self._user_gateway.get_by_user_id(user_id=UserID(data.user_id))
        if user is None:
            return

        await self._entity_saver.delete(user)
        await self._transaction_db.commit()
