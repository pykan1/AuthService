from typing import Any

from pydantic import BaseModel

from container import Container


class Settings(BaseModel):
    authjwt_secret_key: str = Container().auth["secret_key"]


class RegAuthModel(BaseModel):
    id_role: int
    login: str
    password: str


class Items(BaseModel):
    access_token: str
    favorite: str
    basket: str


class PersonResponse(BaseModel):
    __login: str
    __role: int
    __favorite: str | None
    __basket: str | None
    __access_token: str

    def __init__(self,
                 login: str,
                 role: int,
                 favorite: str | None,
                 basket: str | None,
                 access_token: str,
                 **data: Any):
        super().__init__(**data)
        self.__login = login
        self.__role = role
        self.__favorite = favorite
        self.__basket = basket
        self.__access_token = access_token

    def get_login(self):
        return self.__login

    def get_favorite(self):
        return self.__favorite

    def get_basket(self):
        return self.__basket

    def get_access_token(self):
        return self.__access_token

    def get_role(self):
        return self.__role

    login = property(get_login)
    role = property(get_role)
    favorite = property(get_favorite)
    basket = property(get_basket)
    access_token = property(get_access_token)
