from unittest.mock import Mock

import pytest

from application.commands.user.delete_user.dtos import DeleteUserCommand
from application.commands.user.delete_user.handler import DeleteUserCommandHandler
from domains.user.enums import UserRole
from domains.user.models import User
from domains.user.value_objects import UserEmail


@pytest.mark.commands
@pytest.mark.parametrize(
    "dto",
    [
        DeleteUserCommand("access_token"),
    ],
)
async def test_delete_user(
        dto: DeleteUserCommand,
        fake_transaction_db: Mock,
        fake_entity_saver: Mock,
        fake_user_gateway: Mock,
        fake_jwt_service: Mock,
) -> None:
    interactor = DeleteUserCommandHandler(
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

    assert response is None
