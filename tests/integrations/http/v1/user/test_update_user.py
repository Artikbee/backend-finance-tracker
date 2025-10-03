from httpx import AsyncClient


async def test_update_user_success(client: AsyncClient) -> None:
    payload = {
        "email": "user123034@example.com",
        "password": "1234"
    }
    response = await client.post("/v1/users/register", json=payload)
    assert response.status_code == 200

    response = await client.post("/v1/users/login", json=payload)
    assert response.status_code == 200

    access_token = response.json()['access_token']
    payload = {
        "last_name": "string1",
        "first_name": "string",
        "is_active": True
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = await client.put("/v1/users/", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()['last_name'] == "string1"
    assert response.json()['first_name'] == "string"
    assert response.json()['is_active'] == True
