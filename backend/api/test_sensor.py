import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_createSensor(client):
    #make user
    User.objects.create_user(
        username="testuser",
        email="t@t.com",
        password="pass1234",
    )
	#login
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
    #the above is taken from test_auth test_login_success so it should work
    token =data["token"]
	#try to use the jwt path with the token
    sensor_response = client.post(
        "/api/sensors",
        {
            "name": "device-001",
            "model": "EnviroSense",
            "description": "Test sensor",
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {token}",
    )
    assert sensor_response.status_code == 200
    sensor_data = sensor_response.json()

    assert sensor_data["name"] == "device-001"
    assert sensor_data["model"] == "EnviroSense"
    assert sensor_data["description"] == "Test sensor" or sensor_data["description"] is None
