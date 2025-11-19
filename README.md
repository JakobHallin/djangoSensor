
# How to start the project
## Start PostgreSQL
```
docker compose up -d
```
## Set up environment
Create and activate virtual environment
```
python3 -m venv ~/.virtualenvs/djangodev
source ~/.virtualenvs/djangodev/bin/activate
```
Install dependencies
```
pip install django
pip install "psycopg[binary]" -vvv
pip install django-ninja
pip install djangorestframework-simplejwt
pip install pytest pytest-django -vvv
```
## Apply database migrations
```
cd backend
python3 manage.py makemigrations 
python3 manage.py migrate
```
## Run the server
```
python3 manage.py runserver
```
Available at:
```
http://localhost:8000/
127.0.0.1:8000/
```
## Run tests
```
python -m pytest -v
```
## Implemented tests
Did not have time to implement all the tests 
* implemented api/test_auth.py
* create sensor api/test_sensor.py

I missed tests for Sensor and for Readings.
## API documentation 
```
127.0.0.1:8000/api/docs
http://localhost:8000/api/docs 
```
## API endpoints

All endpoints are prefixed with `/api`.

I did not have time to implement pagination or date-range filters for readings.

### Auth (no refresh token)

- `POST /api/auth/register/` — register. Request: email, username, password. Response: token + user summary. 
- `POST /api/auth/token/` — login. Request: email, password. Response: token. 
- `POST /api/auth/refresh/` — (if using JWT) (Not implemented)

### Sensors (Auth required)

- `GET /api/sensors/` — list
- `POST /api/sensors/` — create. Body: name, model, description (optional).
- `GET /api/sensors/{sensor_id}/` — detail.
- `PUT /api/sensors/{sensor_id}/` — update.
- `DELETE /api/sensors/{sensor_id}/` — delete (cascade readings).

### Readings (Auth required)

- `GET /api/sensors/{sensor_id}/readings/` — list readings for a sensor
- `POST /api/sensors/{sensors_id}/readings/` — create. Body: temperature, humidity, timestamp.
