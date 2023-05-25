from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from model import RegAuthModel, Settings
from repository import Repository
from service import Service

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
