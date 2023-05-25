import datetime

import jwt
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from container import Container


class TokenRepository(BaseModel):
    __expires: datetime.timedelta = datetime.timedelta(days=3)

    @staticmethod
    def get_login(token: str) -> str:
        return jwt.decode(
            jwt=token,
            key=Container().auth["secret_key"],
            algorithms=["HS256"]
        )["sub"]

    def create_access_token(self, login: str) -> str:
        access_token = AuthJWT().create_access_token(subject=login, expires_time=self.__expires)
        return access_token

    @staticmethod
    def create_refresh_token(login: str, Authorize: AuthJWT = AuthJWT()) -> str:
        return Authorize.create_refresh_token(subject=login)
