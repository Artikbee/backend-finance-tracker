from unittest.mock import Mock

import pytest

from application.commands.user.logout_user.dtos import LogoutUserCommand, LogoutUserCommandResponse
from application.commands.user.logout_user.handler import LogoutUserCommandHandler


@pytest.mark.commands
@pytest.mark.parametrize(
    "dto",
    [
        LogoutUserCommand("refresh_token"),
    ],
)
async def test_logout_user(
        dto: LogoutUserCommand,
        fake_transaction_db: Mock,
        fake_entity_saver: Mock,
        fake_user_gateway: Mock,
        fake_jwt_service: Mock,
) -> None:
    interactor = LogoutUserCommandHandler(
        user_gateway=fake_user_gateway,
        transaction_db=fake_transaction_db,
        entity_saver=fake_entity_saver,
        jwt_service=fake_jwt_service,
    )
    response = await interactor.run(dto)

    assert isinstance(response, LogoutUserCommandResponse)
    assert response.message == "Logout successful"
