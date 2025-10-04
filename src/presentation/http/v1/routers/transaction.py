from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path

from application.commands.transaction.create_transaction.dtos import CreateTransactionCommand, \
    CreateTransactionCommandResponse
from application.commands.transaction.create_transaction.handler import CreateTransactionCommandHandler
from application.queries.transaction.get_transactions.dtos import GetTransactionsQuery
from application.queries.transaction.get_transactions.handler import GetTransactionsQueryHandler
from domains.account.models import AccountID
from domains.category.models import CategoryID
from domains.transaction.value_objects import TransactionDescription
from presentation.http.v1.__common__.dependencies import CredentialsDependency
from presentation.http.v1.__common__.schemas.transaction import CreateTransactionSchema

router = APIRouter(prefix="/accounts", tags=["Transactions"], route_class=DishkaRoute)


@router.post("/{account_id}/transactions/")
async def create_transaction(
        account_id: Annotated[AccountID, Path(alias="account_id")],
        request_data: CreateTransactionSchema,
        interactor: FromDishka[CreateTransactionCommandHandler],
        credentials: CredentialsDependency,
) -> CreateTransactionCommandResponse:
    dto = CreateTransactionCommand(
        access_token=credentials.credentials,
        account_id=account_id,
        category_id=CategoryID(request_data.category_id),
        transaction_type=request_data.transaction_type,
        amount=request_data.amount,
        description=TransactionDescription(request_data.description),
    )
    return await interactor.run(dto)


@router.get("/{account_id}/transactions/")
async def get_transactions(
        account_id: Annotated[AccountID, Path(alias="account_id")],
        interactor: FromDishka[GetTransactionsQueryHandler],
        credentials: CredentialsDependency,
):
    dto = GetTransactionsQuery(
        access_token=credentials.credentials,
        account_id=account_id,
    )
    return await interactor.run(dto)
