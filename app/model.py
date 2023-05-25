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

    def get_return(self):
        return self

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

    def set_login(self, new: str):
        self.__login = new

    def set_favorite(self, new: str):
        self.__favorite = new

    def set_basket(self, new: str):
        self.__basket = new

    def set_access_token(self, new: str):
        self.__access_token = new

    def set_role(self, new: int):
        self.__role = new

    login = property(get_login, set_login)
    role = property(get_role, set_role)
    favorite = property(get_favorite, set_favorite)
    basket = property(get_basket, set_basket)
    access_token = property(get_access_token, set_access_token)
