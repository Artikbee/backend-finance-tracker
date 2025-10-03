from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from application.commands.account.create_account.dtos import CreateAccountCommandResponse, CreateAccountCommand
from application.commands.account.create_account.handler import CreateAccountCommandHandler
from application.queries.account.get_accounts.dtos import GetAccountsQueryResponse, GetAccountsQuery
from application.queries.account.get_accounts.handler import GetAccountsQueryHandler
from domains.account.value_objects import AccountName
from presentation.http.v1.__common__.dependencies import CredentialsDependency
from presentation.http.v1.__common__.schemas.account import CreateAccountSchema

router = APIRouter(prefix="/accounts", tags=["Accounts"], route_class=DishkaRoute)


@router.post("/")
async def create_account(
        request_data: CreateAccountSchema,
        interactor: FromDishka[CreateAccountCommandHandler],
        credentials: CredentialsDependency,
) -> CreateAccountCommandResponse:
    dto = CreateAccountCommand(
        access_token=credentials.credentials,
        name=AccountName(request_data.name),
        account_type=request_data.account_type,
        currency=request_data.currency,
        balance=request_data.balance,
    )
    return await interactor.run(dto)


@router.get("/{account_id}")
async def get_account(
        request_data: CreateAccountSchema,
) -> None:
    ...


@router.get("/")
async def get_accounts(
        interactor: FromDishka[GetAccountsQueryHandler],
        credentials: CredentialsDependency,
) -> GetAccountsQueryResponse:
    dto = GetAccountsQuery(
        access_token=credentials.credentials,
    )
    return await interactor.run(dto)


@router.put("/{account_id}")
async def update_account(
        request_data: CreateAccountSchema,
) -> None:
    ...


@router.delete("/{account_id}")
async def delete_account(
        request_data: CreateAccountSchema,
) -> None:
    ...
