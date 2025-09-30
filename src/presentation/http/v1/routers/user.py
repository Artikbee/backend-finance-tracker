from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from application.commands.user.register_user import (
    RegisterUserCommandHandler,
    RegisterUserCommand,
    RegisterUserCommandResponse,
)
from domains.user.value_objects import UserEmail
from presentation.http.v1.__common__.schemas.user import RegisterUserSchema

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
async def login_user() -> str:
    return "Hello World"


@router.post("/logout")
async def logout_user() -> str:
    return "Hello World"


@router.put("/")
async def update_user() -> str:
    return "Hello World"


@router.delete("/{user_id}")
async def delete_user() -> str:
    return "Hello World"
