from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path

from application.commands.account.create_account.dtos import CreateAccountCommandResponse, CreateAccountCommand
from application.commands.account.create_account.handler import CreateAccountCommandHandler
from application.commands.account.delete_account.dtos import DeleteAccountCommand
from application.commands.account.delete_account.handler import DeleteAccountCommandHandler
from application.commands.account.update_account.dtos import UpdateAccountCommand, UpdateAccountCommandResponse
from application.commands.account.update_account.handler import UpdateAccountCommandHandler
from application.queries.account.get_account_by_id.dtos import GetAccountByIDQueryResponse, GetAccountByIDQuery
from application.queries.account.get_account_by_id.handler import GetAccountByIDQueryHandler
from application.queries.account.get_accounts.dtos import GetAccountsQueryResponse, GetAccountsQuery
from application.queries.account.get_accounts.handler import GetAccountsQueryHandler
from domains.account.models import AccountID
from domains.account.value_objects import AccountName
from presentation.http.v1.__common__.dependencies import CredentialsDependency
from presentation.http.v1.__common__.schemas.account import CreateAccountSchema, UpdateAccountSchema

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
async def get_account_by_id(
        account_id: Annotated[AccountID, Path(alias="account_id")],
        interactor: FromDishka[GetAccountByIDQueryHandler],
        credentials: CredentialsDependency,
) -> GetAccountByIDQueryResponse:
    dto = GetAccountByIDQuery(
        access_token=credentials.credentials,
        account_id=account_id,
    )
    return await interactor.run(dto)


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
        request_data: UpdateAccountSchema,
        account_id: Annotated[AccountID, Path(alias="account_id")],
        interactor: FromDishka[UpdateAccountCommandHandler],
        credentials: CredentialsDependency,
) -> UpdateAccountCommandResponse:
    dto = UpdateAccountCommand(
        access_token=credentials.credentials,
        account_id=account_id,
        name=AccountName(request_data.name),
        account_type=request_data.account_type,
        currency=request_data.currency,
        is_active=request_data.is_active,
    )
    return await interactor.run(dto)


@router.delete("/{account_id}")
async def delete_account(
        account_id: Annotated[AccountID, Path(alias="account_id")],
        interactor: FromDishka[DeleteAccountCommandHandler],
        credentials: CredentialsDependency,
) -> None:
    dto = DeleteAccountCommand(
        access_token=credentials.credentials,
        account_id=account_id,
    )
    return await interactor.run(dto)
