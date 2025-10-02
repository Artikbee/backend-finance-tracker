import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
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
            jwt_service: JWTService,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver
        self._jwt_service = jwt_service

    async def run(self, data: LogoutUserCommand) -> LogoutUserCommandResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.refresh_token,
            expected_type="refresh",
        )
        user = await self._user_gateway.get_by_user_id(user_id=user_id)

        # add blacklist table

        return LogoutUserCommandResponse(
            message="Logout successful",
        )
