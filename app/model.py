from typing import Any

from pydantic import BaseModel


class PersonResponse(BaseModel):
    __id_person: str
    __login: str
    __favorite: str | None
    __role: str
    __basket: str | None
    __access_token: str

    def __init__(self, id_person, login: str, role: str, favorite: str, basket: str, access_token: str, **data: Any):
        super().__init__(**data)
        self.__id_person = id_person
        self.__login = login
        self.__favorite = favorite
        self.__role = role
        self.__basket = basket
        self.__access_token = access_token


class Items(BaseModel):
    access_token: str
    favorite: str
    basket: str


class PersonRequest(BaseModel):
    __id_person: str
    __login: str
    __favorite: str | None
    __role: str
    __basket: str | None
    __access_token: str
    __refresh_token: str
    __password: str

    def __init__(self,
                 login: str,
                 role: str,
                 favorite: str,
                 basket: str,
                 access_token: str,
                 password: str,
                 refresh_token: str,
                 **data: Any):
        super().__init__(**data)
        self.__login = login
        self.__favorite = favorite
        self.__role = role
        self.__basket = basket
        self.__password = password
        self.__refresh_token = refresh_token
        self.__access_token = access_token

    def get_id_person(self):
        return self.__id_person

    def get_login(self):
        return self.__login

    def get_favorite(self):
        return self.__favorite

    def get_role(self):
        return self.__role

    def get_basket(self):
        return self.__basket

    def get_access_token(self):
        return self.__access_token

    def get_refresh_token(self):
        return self.__refresh_token

    def get_password(self):
        return self.__password

    def set_password(self, new: str):
        self.__password = new

    id_person = property(get_id_person)
    login = property(get_login)
    favorite = property(get_favorite)
    role = property(get_role)
    basket = property(get_basket)
    refresh_token = property(get_refresh_token)
    access_token = property(get_access_token)
    password = property(get_password, set_password)
