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
    login: str = ""
    role: int = 1
    favorite: str | None
    basket: str | None
    access_token: str = ""

    def get_model(
            self,
            login: str,
            id_role: int,
            access_token: str,
            basket: str,
            favorite: str
    ):
        self.login = login
        self.role = id_role
        self.access_token = access_token
        self.basket = basket
        self.favorite = favorite
