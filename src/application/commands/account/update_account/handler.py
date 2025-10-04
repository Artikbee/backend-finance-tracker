import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.validators.account_not_found import validate_account_not_found
from application.__common__.validators.user_not_found import validate_user_not_found
from application.commands.account.update_account.dtos import UpdateAccountCommand, UpdateAccountCommandResponse

logger = logging.getLogger(__name__)


class UpdateAccountCommandHandler:
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

    async def run(self, data: UpdateAccountCommand) -> UpdateAccountCommandResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type='access',
        )
        user = await self._user_gateway.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        account = await self._account_gateway.get_by_account_id_and_user_id(
            user_id=user.oid,
            account_id=data.account_id,
        )
        validate_account_not_found(account)

        account.update_name(data.name)
        account.update_account_type(data.account_type)
        account.update_currency(data.currency)
        account.update_is_active(data.is_active)

        await self._transaction_db.flush()
        await self._transaction_db.commit()

        return UpdateAccountCommandResponse(
            account_id=account.oid,
            name=account.name.value,
            account_type=account.account_type,
            currency=account.currency,
            balance=account.balance,
            is_active=user.is_active,
        )
