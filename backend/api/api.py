# backend/api/api.py
from ninja import NinjaAPI
from django.contrib.auth.models import User
from ninja import Schema

api = NinjaAPI()

class UserIn(Schema):
    name: str
    #lastname: str
    email: str
    password: str

@api.get("/health")
def health(request):
    return {"status": "ok"}
@api.get("/users")
def getUser(request):
	users = User.objects.values()
	return list(users)
@api.post("/createUser")
def creatUser(request, payload: UserIn):
    user = User.objects.create_user(
        username=payload.name,
        email=payload.email,
        password=payload.password,
    )
    #user.first_name = payload.name
    #user.last_name = payload.lastname
    user.save()
#@api.auth("/auth/register"

