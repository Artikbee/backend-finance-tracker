import logging

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.category.reader import CategoryReader
from application.__common__.ports.persistence.user.reader import UserReader
from application.__common__.validators.user_not_found import validate_user_not_found
from application.queries.category.get_categories.dtos import GetCategoriesQuery, GetCategoriesQueryResponse

logger = logging.getLogger(__name__)


class GetCategoriesQueryHandler:
    def __init__(
            self,
            user_reader: UserReader,
            jwt_service: JWTService,
            category_reader: CategoryReader,
    ) -> None:
        self._user_reader = user_reader
        self._jwt_service = jwt_service
        self._category_reader = category_reader

    async def run(self, data: GetCategoriesQuery) -> GetCategoriesQueryResponse:
        user_id = await self._jwt_service.verify_and_get_user_id(
            token=data.access_token,
            expected_type="access"
        )
        user = await self._user_reader.get_by_user_id(user_id=user_id)
        validate_user_not_found(user)

        categories = await self._category_reader.get_all_by_user_id(user_id=user.oid)

        return GetCategoriesQueryResponse.create_model(categories)
