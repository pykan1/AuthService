from fastapi import APIRouter, Depends

from model import RegAuthModel
from service import Service

auth_service = APIRouter(
    tags=["Authorization"],
    responses={404: {"description": "Not found"}},
)


@auth_service.post("/register")
async def register(
        user: RegAuthModel,
        service: Service = Depends()):
    return service.register(user)
