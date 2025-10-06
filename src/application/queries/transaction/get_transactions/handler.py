import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.reader import AccountReader
from application.__common__.ports.persistence.category.reader import CategoryReader
from application.__common__.ports.persistence.transaction.reader import TransactionReader
from application.__common__.ports.persistence.user.reader import UserReader
from application.__common__.validators.account_not_found import validate_account_not_found
from application.__common__.validators.user_not_found import validate_user_not_found
from application.queries.transaction.get_transactions.dtos import GetTransactionsQuery, GetTransactionQueryResponse, \
    GetTransactionsQueryResponse

logger = logging.getLogger(__name__)


class GetTransactionsQueryHandler:
    def __init__(
            self,
            user_reader: UserReader,
            account_reader: AccountReader,
            jwt_service: JWTService,
            category_reader: CategoryReader,
            transaction_reader: TransactionReader,
    ) -> None:
        self._user_reader = user_reader
        self._jwt_service = jwt_service
        self._category_reader = category_reader
        self._account_reader = account_reader
        self._transaction_reader = transaction_reader

    async def run(self, data: GetTransactionsQuery) -> GetTransactionsQueryResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access"
        )
        user = await self._user_reader.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        account = await self._account_reader.get_by_account_id_and_user_id_join_transaction(
            account_id=data.account_id,
            user_id=user.oid
        )
        validate_account_not_found(account)

        transactions = await self._transaction_reader.get_all_by_account_id(
            account_id=account.oid
        )

        transaction_res = []
        for i in transactions:
            category = await self._category_reader.get_by_category_id(
                category_id=i.category_id,
            )
            transaction_res.append(
                GetTransactionQueryResponse(
                    category_name=category.name.value,
                    transaction_type=i.transaction_type,
                    amount=i.amount,
                    description=i.description.value,
                )
            )

        return GetTransactionsQueryResponse(
            transactions=transaction_res
        )
