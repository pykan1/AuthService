import datetime

import jwt
from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from container import Container


class TokenRepository(BaseModel):
    __expires: datetime.timedelta = datetime.timedelta(days=3)

    @staticmethod
    def get_token_data(token) -> dict:
        try:
            user = jwt.decode(
                jwt=token,
                key=Container().auth["secret_key"],
                algorithms=["HS256"]
            )
            print(user)
            return user
        except:
            raise HTTPException(status_code=403, detail="token expired")

    def create_access_token(self, login: str, uuid: str, id_role: int) -> str:
        access_token = AuthJWT().create_access_token(user_claims={
            "uuid": str(uuid),
            "id_role": int(id_role)
        }, expires_time=self.__expires, subject=login)
        return access_token

    @staticmethod
    def create_refresh_token(login: str, uuid: str, id_role: int, Authorize: AuthJWT = AuthJWT()) -> str:
        return Authorize.create_refresh_token(user_claims={
            "uuid": uuid,
            "id_role": id_role
        }, subject=login)
