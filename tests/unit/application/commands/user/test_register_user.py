from unittest.mock import Mock

import pytest

from application.__common__.errors.base_errors import ConflictError
from application.__common__.errors.user_already_exists import UserAlreadyExistsError
from application.commands.user.register_user.dtos import RegisterUserCommand
from application.commands.user.register_user.handler import RegisterUserCommandHandler
from domains.user.value_objects import UserEmail


@pytest.mark.parametrize(
    ("dto", "exc_class"),
    [
        (RegisterUserCommand(UserEmail("fake@email.com"), "1234567"), None),
        (RegisterUserCommand(UserEmail("fake2@email.com"), "1234567"), UserAlreadyExistsError),
    ],
)
async def test_register_user(
        dto: RegisterUserCommand,
        exc_class: type[ConflictError] | None,
        fake_transaction_db: Mock,
        fake_entity_saver: Mock,
        fake_user_gateway: Mock,
        fake_password_hasher_service: Mock,
) -> None:
    interactor = RegisterUserCommandHandler(
        user_gateway=fake_user_gateway,
        transaction_db=fake_transaction_db,
        entity_saver=fake_entity_saver,
        password_hasher_service=fake_password_hasher_service,
    )
    if exc_class:
        fake_user_gateway.get_by_email.return_value = dto.email
        with pytest.raises(exc_class) as excinfo:
            _ = await interactor.run(dto)

        assert excinfo.value.message == "User already exists"
        assert isinstance(excinfo.value, UserAlreadyExistsError)
    else:
        response = await interactor.run(dto)

        assert response.message == "Check your email"
        fake_user_gateway.get_by_email.assert_called_once()
        fake_entity_saver.add_one.assert_called_once()
        fake_transaction_db.commit.assert_called_once()
