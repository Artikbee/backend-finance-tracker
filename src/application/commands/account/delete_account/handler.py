import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.commands.account.delete_account.dtos import DeleteAccountCommand

logger = logging.getLogger(__name__)


class DeleteAccountCommandHandler:
    def __init__(
            self,
            user_gateway: UserGateway,
            account_gateway: AccountGateway,
            transaction_db: TransactionDB,
            entity_saver: EntitySaver,
            jwt_service: JWTService,
    ) -> None:
        self._user_gateway = user_gateway
        self._transaction_db = transaction_db
        self._entity_saver = entity_saver
        self._jwt_service = jwt_service
        self._account_gateway = account_gateway

    async def run(self, data: DeleteAccountCommand) -> None:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access",
        )
        user = await self._user_gateway.get_by_user_id(user_id=user_id)
        if user is None:
            return

        account = await self._account_gateway.get_by_account_id_and_user_id(
            user_id=user.oid,
            account_id=data.account_id,
        )
        if account is None:
            return

        await self._entity_saver.delete(account)
        await self._transaction_db.commit()
