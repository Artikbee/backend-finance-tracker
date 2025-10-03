import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.account.reader import AccountReader
from application.__common__.ports.persistence.user.reader import UserReader
from application.__common__.validators.user_not_found import validate_user_not_found
from application.queries.account.get_accounts.dtos import GetAccountsQuery, GetAccountsQueryResponse

logger = logging.getLogger(__name__)


class GetAccountsQueryHandler:
    def __init__(
            self,
            user_reader: UserReader,
            jwt_service: JWTService,
            account_reader: AccountReader,
    ) -> None:
        self._user_reader = user_reader
        self._jwt_service = jwt_service
        self._account_reader = account_reader

    async def run(self, data: GetAccountsQuery) -> GetAccountsQueryResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access"
        )
        user = await self._user_reader.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        accounts = await self._account_reader.get_all_by_user_id(user_id=user.oid)

        return GetAccountsQueryResponse.create_model(accounts)
