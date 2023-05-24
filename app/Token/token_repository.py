import datetime

import jwt
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from container import Container


class TokenRepository:
    __expires: datetime.timedelta = datetime.timedelta(days=3)

    @staticmethod
    def get_login(token: str) -> str:
        return jwt.decode(
            jwt=token,
            key=Container().auth["secret_key"],
            algorithms=["HS256"]
        )["sub"]

    def create_access_token(self, login: str, Authorize: AuthJWT = Depends()) -> str:
        return Authorize.create_access_token(subject=login, expires_time=self.__expires)

    @staticmethod
    def create_refresh_token(login: str, Authorize: AuthJWT = Depends()) -> str:
        return Authorize.create_refresh_token(subject=login)
