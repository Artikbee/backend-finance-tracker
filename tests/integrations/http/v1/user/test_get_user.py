from httpx import AsyncClient


async def test_get_user_success(client: AsyncClient) -> None:
    payload = {
        "email": "user1230345@example.com",
        "password": "1234"
    }
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200

    response = await client.post("/v1/users/login", json=payload)
    assert response.status_code == 200

    access_token = response.json()['access_token']
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = await client.get("/v1/users/", headers=headers)
    assert response.status_code == 200
    assert response.json()['last_name'] is None
    assert response.json()['first_name'] is None
    assert response.json()['is_active'] == True
