

starta postgress
docker compose up -d

Starta django 
First set up enviorment
python3 -m venv ~/.virtualenvs/djangodev
source ~/.virtualenvs/djangodev/bin/activate

pip install django
pip install "psycopg[binary]" -vvv
pip install django-ninja
pip install djangorestframework-simplejwt

python3 manage.py makemigrations 
python3 manage.py migrate

sudo apt install python3-pytest
pip install pytest pytest-django -vvv

starta
python3 manage.py runserver
tilgänglig på
http://localhost:8000/
127.0.0.1:8000/

testa
backend$ python -m pytest -v

kolla structuren på 
127.0.0.1:8000/api/docs


## API endpoints

All endpoints are prefixed with `/api`.

### Auth

- `POST /api/auth/register/` — register. Request: email, username, password. Response: token + user summary. # Dont give refresh tocken
- `POST /api/auth/token/` — login. Request: email, password. Response: token. #Respons token just one not refresh token
- `POST /api/auth/refresh/` — (if using JWT) #not implemented

### Sensors (Auth required)

- `GET /api/sensors/` — list
- `POST /api/sensors/` — create. Body: name, model, description (optional).
- `GET /api/sensors/{sensor_id}/` — detail.
- `PUT /api/sensors/{sensor_id}/` — update.
- `DELETE /api/sensors/{sensor_id}/` — delete (cascade readings).

### Readings (Auth required)

- `GET /api/sensors/{sensor_id}/readings/` — list readings for a sensor
- `POST /api/sensors/{sensors_id}/readings/` — create. Body: temperature, humidity, timestamp.
