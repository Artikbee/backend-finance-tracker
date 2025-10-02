from httpx import AsyncClient


async def test_register_user_success(client: AsyncClient) -> None:
    payload = {
        "email": "user7777@example.com",
        "password": "1234"
    }
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Check your email"}
