from unittest.mock import AsyncMock, Mock

import pytest

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway


@pytest.fixture
def fake_jwt_service() -> JWTService:
    fake = Mock()
    fake.generate = AsyncMock()
    fake.get_expires_time = AsyncMock()
    return fake


@pytest.fixture
def fake_transaction_db() -> TransactionDB:
    fake = Mock()
    fake.commit = AsyncMock()
    fake.flush = AsyncMock()
    return fake


@pytest.fixture
def fake_entity_saver() -> EntitySaver:
    fake = Mock()
    fake.add_one = Mock()
    fake.delete = AsyncMock()
    return fake


@pytest.fixture
def fake_user_gateway() -> UserGateway:
    fake = Mock()
    fake.get_by_email = AsyncMock(return_value=None)
    fake.get_by_email_and_password = AsyncMock(return_value=None)
    return fake
