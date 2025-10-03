import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.validators.user_not_found import validate_user_not_found
from application.commands.account.create_account.dtos import CreateAccountCommand, CreateAccountCommandResponse
from domains.account.models import Account

logger = logging.getLogger(__name__)


class CreateAccountCommandHandler:
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

    async def run(self, data: CreateAccountCommand) -> CreateAccountCommandResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type='access',
        )
        user = await self._user_gateway.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        new_account = Account.create(
            user_id=user.oid,
            name=data.name,
            account_type=data.account_type,
            currency=data.currency,
            balance=data.balance,
            is_active=True,
        )
        self._entity_saver.add_one(new_account)
        await self._transaction_db.commit()

        return CreateAccountCommandResponse(
            account_id=new_account.oid
        )
