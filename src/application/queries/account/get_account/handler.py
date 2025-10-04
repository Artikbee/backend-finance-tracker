import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.reader import AccountReader
from application.__common__.ports.persistence.user.reader import UserReader
from application.__common__.validators.account_not_found import validate_account_not_found
from application.__common__.validators.user_not_found import validate_user_not_found
from application.queries.account.get_account.dtos import GetAccountQuery, GetAccountQueryResponse

logger = logging.getLogger(__name__)


class GetAccountQueryHandler:
    def __init__(
            self,
            user_reader: UserReader,
            account_reader: AccountReader,
            jwt_service: JWTService,
    ) -> None:
        self._user_reader = user_reader
        self._jwt_service = jwt_service
        self._account_reader = account_reader

    async def run(self, data: GetAccountQuery) -> GetAccountQueryResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access"
        )
        user = await self._user_reader.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        account = await self._account_reader.get_by_account_id_and_user_id(
            account_id=data.account_id,
            user_id=user.oid,
        )
        validate_account_not_found(account)

        return GetAccountQueryResponse(
            account_id=account.oid,
            name=account.name.value,
            account_type=account.account_type,
            currency=account.currency,
            balance=account.balance,
            is_active=account.is_active,
        )
