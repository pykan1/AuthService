from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from database.database_repository import DatabaseRepository
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
        user: RegAuthModel,
        db: Session = Depends(DatabaseRepository().get_db)
):
    service = Service(Repository())
    return service.register(user, db)


@auth_service.post("/login")
async def login(
        user: RegAuthModel,
        db: Session = Depends(DatabaseRepository().get_db)
):
    service = Service(Repository())
    return service.login(user, db)


@auth_service.post("/update_refresh_token")
async def new_access_token(
        refresh_token: str,
        db: Session = Depends(DatabaseRepository().get_db)
):
    service = Service(Repository())
    return service.update_access_token(refresh_token, db)
