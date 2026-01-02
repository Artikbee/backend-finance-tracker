from unittest.mock import Mock

import pytest

from application.commands.user.update_user.dtos import UpdateUserCommand, UpdateUserCommandResponse
from application.commands.user.update_user.handler import UpdateUserCommandHandler
from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import UserLastName, UserFirstName, UserEmail


@pytest.mark.commands
@pytest.mark.parametrize(
    "dto",
    [
        UpdateUserCommand(
            "access_token",
            UserLastName("WWWW"),
            UserFirstName('qqww'),
            True,
        ),
    ],
)
async def test_update_user(
        dto: UpdateUserCommand,
        fake_transaction_db: Mock,
        fake_entity_saver: Mock,
        fake_user_gateway: Mock,
        fake_jwt_service: Mock,
) -> None:
    interactor = UpdateUserCommandHandler(
        user_gateway=fake_user_gateway,
        transaction_db=fake_transaction_db,
        entity_saver=fake_entity_saver,
        jwt_service=fake_jwt_service,
    )
    fake_user = User.create(
        email=UserEmail("fake@email.com"),
        hashed_password="123",
        first_name=None,
        last_name=None,
        role=UserRole.USER,
        is_active=True,
    )
    fake_user_gateway.get_by_user_id.return_value = fake_user
    response = await interactor.run(dto)

    assert isinstance(response, UpdateUserCommandResponse)
    assert response.last_name == dto.last_name.value
