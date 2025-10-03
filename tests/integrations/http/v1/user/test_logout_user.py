from unittest.mock import Mock

from httpx import AsyncClient


async def test_logout_user_success(
        client: AsyncClient,
        user_payload_factory: Mock,
) -> None:
    payload = user_payload_factory("logout_user")
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200

    response = await client.post("/v1/users/login", json=payload)
    assert response.status_code == 200

    payload = {
        "refresh_token": response.json()["refresh_token"],
    }
    response = await client.post("/v1/users/logout", json=payload)
    assert response.status_code == 200
    assert response.json()['message'] == 'Logout successful'
