import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.commands.user.login_user.dtos import (
    LoginUserCommand,
    LoginUserCommandResponse,
)

logger = logging.getLogger(__name__)


class LoginUserCommandHandler:
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

    async def run(self, data: LoginUserCommand) -> LoginUserCommandResponse:
        user = await self._user_gateway.get_by_email_and_password(
            email=data.email,
            hashed_password=data.password,
        )

        access_token, refresh_token = await self._jwt_service.generate(user_id=user.oid)
        access_expires_in, refresh_expires_in = await self._jwt_service.get_expires_time()

        return LoginUserCommandResponse(
            access_token=access_token,
            access_expires_in=access_expires_in,
            refresh_token=refresh_token,
            refresh_expires_in=refresh_expires_in,
            token_type="Bearer",
        )
