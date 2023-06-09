from typing import Any

from pydantic import BaseModel

from container import Container


class Settings(BaseModel):
    authjwt_secret_key: str = Container().auth["secret_key"]


class RefreshTokenModel(BaseModel):
    refresh_token: str = ""


class NumberModel(BaseModel):
    number: str


class RegModel(BaseModel):
    id_role: int
    number: str
    login: str
    password: str


class AuthModel(BaseModel):
    id_role: int
    number: str
    password: str


class Items(BaseModel):
    access_token: str
    favorite: str
    basket: str


class ItemModel(BaseModel):
    id_item: str = ""
    id_category: int = 0
    name: str = ""
    description: str = ""
    reviews: str = ""
    amount: int = 0


class PersonModel(BaseModel):
    id_person: str = ""
    number: str = ""
    login: str = ""
    role: int = 1
    favorite: list = []
    basket: list = []
    orders: list = []
    reviews: list = []
    access_token: str = ""
    refresh_token: str = ""

    def get_model(
            self,
            id_person: str,
            login: str,
            id_role: int,
            access_token: str,
            refresh_token: str,
            basket=None,
            favorite=None,
            orders=None,
            reviews=None,
            number: str = None
    ):
        if reviews is None:
            reviews = []
        if orders is None:
            orders = []
        if basket is None:
            basket = []
        if favorite is None:
            favorite = []
        print(self.favorite)
        self.number = number
        self.id_person = id_person
        self.login = login
        self.role = id_role
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.basket = basket
        self.favorite = favorite
        self.reviews = reviews
        self.orders = orders


