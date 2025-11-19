#test_auth.py
import pytest
from django.contrib.auth.models import User

#Login tests
@pytest.mark.django_db
def test():
	assert "test one"


@pytest.mark.django_db
def test_login_success(client):
    User.objects.create_user(
        username="testuser",
        email="t@t.com",
        password="pass1234",
    )
    response = client.post(
        "/api/auth/token",
        {
            "email": "t@t.com",
            "password": "pass1234",
        },
        content_type="application/json",
    )

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str) and data["token"] != ""


@pytest.mark.django_db
def test_login_wrongEmail(client):
    User.objects.create_user(
        username="testuser",
        email="t@t.com",
        password="pass1234",
    )
    response = client.post(
        "/api/auth/token",
        {
            "email": "x@t.com",
            "password": "pass1234",
        },
        content_type="application/json",
    )

    assert response.status_code == 401
    data = response.json()
    assert "detail" in data

@pytest.mark.django_db
def test_login_wrongPassword(client):
    User.objects.create_user(
        username="testuser",
        email="t@t.com",
        password="pass1234",
    )
    response = client.post(
        "/api/auth/token",
        {
            "email": "t@t.com",
            "password": "x",
        },
        content_type="application/json",
    )

    assert response.status_code == 401
    data = response.json()
    assert "detail" in data

@pytest.mark.django_db
def test_register_success(client):
    response = client.post(
        "/api/auth/register",
        {
            "name": "testuser",
            "email": "t@t.com",
            "password": "pass1234",
        },
        content_type="application/json",
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == "t@t.com"

@pytest.mark.django_db
def test_register_noEmail(client):
    response = client.post(
        "/api/auth/register",
        {
            "name": "testuser",
            "password": "pass1234",
        },
        content_type="application/json",
    )
    assert response.status_code == 422


@pytest.mark.django_db
@pytest.mark.xfail(reason="not implemented")
def test_refreshToken(client):
    User.objects.create_user(
        username="testuser",
        email="t@t.com",
        password="pass1234",
    )
    response = client.post(
        "/api/auth/token",
        {
            "email": "t@t.com",
            "password": "pass1234",
        },
        content_type="application/json",
    )

    assert response.status_code == 200
    data = response.json()
    assert "refresh" in data
    refeshToken=data["refresh"]

    #refesh token with the refresh token
    refreshToken = client.post(
        "/api/auth/refresh",
        {"refresh": refresh_token},
        content_type="application/json",
    )
    #from the spec it should return token
