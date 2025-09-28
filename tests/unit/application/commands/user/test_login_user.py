from unittest.mock import Mock

import pytest

from application.__common__.errors.base_errors import ConflictError
from application.commands.user.login_user.dtos import LoginUserCommand, LoginUserCommandResponse
from application.commands.user.login_user.handler import LoginUserCommandHandler
from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import UserEmail


@pytest.mark.parametrize(
    ("dto", "exc_class"),
    [
        (LoginUserCommand(UserEmail("fake@email.com"), "1234567"), None),
    ],
)
async def test_login_user(
        dto: LoginUserCommand,
        exc_class: type[ConflictError] | None,
        fake_transaction_db: Mock,
        fake_entity_saver: Mock,
        fake_user_gateway: Mock,
        fake_jwt_service: Mock,
) -> None:
    interactor = LoginUserCommandHandler(
        user_gateway=fake_user_gateway,
        transaction_db=fake_transaction_db,
        entity_saver=fake_entity_saver,
        jwt_service=fake_jwt_service,
    )
    if exc_class:
        ...
    else:
        fake_user = User.create(
            email=UserEmail("fake@email.com"),
            hashed_password="123",
            first_name=None,
            last_name=None,
            role=UserRole.USER,
            is_active=True,
        )
        fake_user_gateway.get_by_email_and_password.return_value = fake_user
        fake_jwt_service.generate.return_value = '123', '345'
        fake_jwt_service.get_expires_time.return_value = 1, 2

        response = await interactor.run(dto)
        assert isinstance(response, LoginUserCommandResponse)
        assert response.access_token == "123"
        assert response.refresh_token == "345"
