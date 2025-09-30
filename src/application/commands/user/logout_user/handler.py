import logging

from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.commands.user.logout_user.dtos import (
    LogoutUserCommand,
    LogoutUserCommandResponse,
)

logger = logging.getLogger(__name__)


class LogoutUserCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver

    async def run(self, data: LogoutUserCommand) -> LogoutUserCommandResponse:
        # validate_user_already_exists(...)

        return LogoutUserCommandResponse(
            message="Logout successful",
        )
