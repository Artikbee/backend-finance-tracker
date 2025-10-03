from unittest.mock import Mock

from httpx import AsyncClient


async def test_delete_user_success(
        client: AsyncClient,
        user_payload_factory: Mock,
) -> None:
    payload = user_payload_factory("delete_user")
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200

    response = await client.post("/v1/users/login", json=payload)
    assert response.status_code == 200

    access_token = response.json()['access_token']
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = await client.delete("/v1/users/", headers=headers)
    assert response.status_code == 200
