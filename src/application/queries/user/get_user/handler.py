import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.user.reader import UserReader
from application.queries.user.get_user.dtos import GetUserQuery, \
    GetUserQueryResponse

logger = logging.getLogger(__name__)


class GetUserQueryHandler:
    def __init__(
            self,
            user_reader: UserReader,
            jwt_service: JWTService,
    ) -> None:
        self._user_reader = user_reader
        self._jwt_service = jwt_service

    async def run(self, data: GetUserQuery) -> GetUserQueryResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access"
        )
        user = await self._user_reader.get_by_user_id(user_id=user_id)

        return GetUserQueryResponse(
            email=user.email.value,
            last_name=user.last_name.value,
            first_name=user.first_name.value,
            role=user.role,
            is_active=user.is_active,
        )
