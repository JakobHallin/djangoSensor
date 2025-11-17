# backend/api/api.py
from ninja import NinjaAPI
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ninja import Schema
from django.urls import path, include
from ninja import Router
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
api = NinjaAPI()
#router = Router()
#auth_router = Router()
#auth_urls = [
 #   path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
  #  path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
#]
#api.add_router("/auth", include((auth_urls, "auth"), namespace="auth"))





auth_router = Router(tags=["auth"])

class UserIn(Schema):
    name: str
    #lastname: str
    email: str
    password: str


class LoginIn(Schema):
    email: str
    password: str
class TokenOut(Schema):
    token: str


# Reuse the built-in DRF views
token_obtain_view = TokenObtainPairView.as_view()
token_refresh_view = TokenRefreshView.as_view()

@auth_router.post("/token" , response=TokenOut)
def login(request, payload: LoginIn):
    # 1) Find user by email
    try:
        user = User.objects.get(email=payload.email, is_active=True)
    except User.DoesNotExist:
        return api.create_response(
            request,
            {"detail": "No active account found with the given credentials"},
            status=401,
        )

    # 2) Use SimpleJWT's built-in serializer
    data = {
        "username": user.username,
        "password": payload.password,
    }

    serializer = TokenObtainPairSerializer(data=data)
    try:
        serializer.is_valid(raise_exception=True)
    except AuthenticationFailed as exc:
        return api.create_response(
            request,
            {"detail": str(exc)},
            status=401,
        )

    access = serializer.validated_data["access"]
    return {"token": access}

@auth_router.post("/refresh")
def refresh_token(request):

    return


@auth_router.post("/register")
def auth(request, payload: UserIn):
    user = User.objects.create_user(
        username=payload.name,
        email=payload.email,
        password=payload.password,
    )
    user.save()
    #try to use the same
    data = {
        "username": user.username,
        "password": payload.password,
    }

    serializer = TokenObtainPairSerializer(data=data)
    try:
        serializer.is_valid(raise_exception=True)
    except AuthenticationFailed as exc:
        return api.create_response(
            request,
            {"detail": str(exc)},
            status=401,
        )
    access = serializer.validated_data["access"]
    return {
            "token": access,
            "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
        },}



api.add_router("/auth", auth_router)

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
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username,
    }



