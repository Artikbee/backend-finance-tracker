from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from application.commands.user.delete_user import DeleteUserCommandHandler, DeleteUserCommand
from application.commands.user.login_user import LoginUserCommandHandler, LoginUserCommand, LoginUserCommandResponse
from application.commands.user.logout_user import LogoutUserCommandHandler, LogoutUserCommand, LogoutUserCommandResponse
from application.commands.user.register_user import (
    RegisterUserCommandHandler,
    RegisterUserCommand,
    RegisterUserCommandResponse,
)
from application.commands.user.update_user import UpdateUserCommandHandler, UpdateUserCommand, UpdateUserCommandResponse
from application.queries.user.get_user.dtos import GetUserCommandResponse, GetUserCommand
from application.queries.user.get_user.handler import GetUserQueryHandler
from domains.user.value_objects import UserEmail, UserLastName, UserFirstName
from presentation.http.v1.__common__.dependencies import CredentialsDependency
from presentation.http.v1.__common__.schemas.user import RegisterUserSchema, LoginUserSchema, UpdateUserSchema, \
    LogoutUserSchema

router = APIRouter(prefix="/users", tags=["Users"], route_class=DishkaRoute)


@router.post("/register")
async def register_user(
        request_data: RegisterUserSchema,
        interactor: FromDishka[RegisterUserCommandHandler]
) -> RegisterUserCommandResponse:
    dto = RegisterUserCommand(
        email=UserEmail(request_data.email),
        password=request_data.password,
    )
    return await interactor.run(dto)


@router.post("/login")
async def login_user(
        request_data: LoginUserSchema,
        interactor: FromDishka[LoginUserCommandHandler]
) -> LoginUserCommandResponse:
    dto = LoginUserCommand(
        email=UserEmail(request_data.email),
        password=request_data.password,
    )
    return await interactor.run(dto)


@router.post("/logout")
async def logout_user(
        request_data: LogoutUserSchema,
        interactor: FromDishka[LogoutUserCommandHandler],
) -> LogoutUserCommandResponse:
    dto = LogoutUserCommand(
        refresh_token=request_data.refresh_token,
    )
    return await interactor.run(dto)


@router.put("/")
async def update_user(
        request_data: UpdateUserSchema,
        interactor: FromDishka[UpdateUserCommandHandler],
        credentials: CredentialsDependency,
) -> UpdateUserCommandResponse:
    dto = UpdateUserCommand(
        access_token=credentials.credentials,
        last_name=UserLastName(request_data.last_name),
        first_name=UserFirstName(request_data.first_name),
        is_active=request_data.is_active,
    )
    return await interactor.run(dto)


@router.delete("/")
async def delete_user(
        interactor: FromDishka[DeleteUserCommandHandler],
        credentials: CredentialsDependency,
) -> None:
    dto = DeleteUserCommand(
        access_token=credentials.credentials,
    )
    return await interactor.run(dto)


@router.get("/")
async def get_user(
        interactor: FromDishka[GetUserQueryHandler],
        credentials: CredentialsDependency,
) -> GetUserCommandResponse:
    dto = GetUserCommand(
        access_token=credentials.credentials,
    )
    return await interactor.run(dto)
