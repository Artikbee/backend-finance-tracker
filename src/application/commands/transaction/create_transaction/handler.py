import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.validators.account_not_found import validate_account_not_found
from application.__common__.validators.user_not_found import validate_user_not_found
from application.commands.transaction.create_transaction.dtos import CreateTransactionCommand, \
    CreateTransactionCommandResponse
from domains.transaction.enums import TransactionType
from domains.transaction.models import Transaction

logger = logging.getLogger(__name__)


class CreateTransactionCommandHandler:
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

    async def run(self, data: CreateTransactionCommand) -> CreateTransactionCommandResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type='access',
        )
        user = await self._user_gateway.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        account = await self._account_gateway.get_by_account_id_and_user_id(
            account_id=data.account_id,
            user_id=user.oid,
        )
        validate_account_not_found(account)

        new_transaction = Transaction.create(
            account_id=account.oid,
            category_id=data.category_id,  # need validate
            transaction_type=data.transaction_type,
            amount=data.amount,
            description=data.description,
        )

        self._entity_saver.add_one(new_transaction)

        if new_transaction.transaction_type == TransactionType.INCOME:
            new_balance = account.balance + new_transaction.amount
        else:
            new_balance = account.balance - new_transaction.amount

        account.update_balance(new_balance)

        await self._transaction_db.commit()

        return CreateTransactionCommandResponse(
            transaction_id=new_transaction.oid
        )
