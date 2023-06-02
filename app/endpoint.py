from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from app.model import RegAuthModel, Settings
from app.repository import Repository
from app.service import Service

auth_service = APIRouter(
    tags=["Authorization"],
    responses={404: {"description": "Not found"}},
)


@AuthJWT.load_config
def get_config():
    return Settings()


@auth_service.post("/register")
async def register(
        user: RegAuthModel
):
    service = Service(Repository())
    return service.register(user)


@auth_service.post("/login")
async def login(
        user: RegAuthModel
):
    service = Service(Repository())
    return service.login(user)


@auth_service.post("/update_refresh_token")
async def new_access_token(refresh_token: str):
    service = Service(Repository())
    return service.update_access_token(refresh_token)
