from unittest.mock import Mock

from httpx import AsyncClient


async def test_register_user_success(
        client: AsyncClient,
        user_payload_factory: Mock,
) -> None:
    payload = user_payload_factory("register_user")
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Check your email"}
