from typing import Callable

import pytest


@pytest.fixture
def user_payload_factory() -> Callable[[str], dict[str, str]]:
    def _make_user_payload(email_suffix: str):
        return {
            "email": f"user{email_suffix}@example.com",
            "password": "1234"
        }

    return _make_user_payload

# @pytest.fixture
# async def registered_user(
#         client: AsyncClient,
#         user_payload_factory: Mock
# ):
#     payload = user_payload_factory("test")
#     response = await client.post("/v1/users/register", json=payload)
#     assert response.status_code == 200
#     return payload
#
#
# @pytest.fixture
# async def logged_in_user(
#         client: AsyncClient,
#         registered_user: Mock
# ):
#     response = await client.post("/v1/users/login", json=registered_user)
#     assert response.status_code == 200
#     tokens = response.json()
#     return {
#         "payload": registered_user,
#         "access_token": tokens.get("access_token"),
#         "refresh_token": tokens.get("refresh_token"),
#         "headers": {"Authorization": f"Bearer {tokens.get('access_token')}"}
#     }
