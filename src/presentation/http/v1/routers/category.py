from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from application.commands.category.create_category.dtos import CreateCategoryCommandResponse, CreateCategoryCommand
from application.commands.category.create_category.handler import CreateCategoryCommandHandler
from application.queries.category.get_categories.dtos import GetCategoriesQuery, GetCategoriesQueryResponse
from application.queries.category.get_categories.handler import GetCategoriesQueryHandler
from domains.category.value_objects import CategoryName
from presentation.http.v1.__common__.dependencies import CredentialsDependency
from presentation.http.v1.__common__.schemas.category import CreateCategorySchema

router = APIRouter(prefix="/categories", tags=["Categories"], route_class=DishkaRoute)


@router.post("/")
async def create_category(
        request_data: CreateCategorySchema,
        interactor: FromDishka[CreateCategoryCommandHandler],
        credentials: CredentialsDependency,
) -> CreateCategoryCommandResponse:
    dto = CreateCategoryCommand(
        access_token=credentials.credentials,
        name=CategoryName(request_data.name),
    )
    return await interactor.run(dto)


@router.get("/")
async def get_categories(
        interactor: FromDishka[GetCategoriesQueryHandler],
        credentials: CredentialsDependency,
) -> GetCategoriesQueryResponse:
    dto = GetCategoriesQuery(
        access_token=credentials.credentials,
    )
    return await interactor.run(dto)
