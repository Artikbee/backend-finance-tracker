from httpx import AsyncClient


async def test_login_user_success(client: AsyncClient) -> None:
    payload = {
        "email": "user1230@example.com",
        "password": "1234"
    }
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200

    response = await client.post("/v1/users/login", json=payload)
    assert response.status_code == 200
