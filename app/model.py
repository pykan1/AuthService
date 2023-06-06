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


class ItemModel(BaseModel):
    id_item: str = ""
    id_category: int = 0
    name: str = ""
    description: str = ""
    reviews: str = ""
    amount: int = 0


class PersonModel(BaseModel):
    id_person: str = ""
    login: str = ""
    role: int = 1
    favorite: list = []
    basket: list = []
    orders: list = []
    reviews: list = []
    access_token: str = ""

    def get_model(
            self,
            id_person: str,
            login: str,
            id_role: int,
            access_token: str,
            basket=None,
            favorite=None,
            orders=None,
            reviews=None
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
        self.id_person = id_person
        self.login = login
        self.role = id_role
        self.access_token = access_token
        self.basket = basket
        self.favorite = favorite
        self.reviews = reviews
        self.orders = orders


class PersonResponse(BaseModel):
    person: PersonModel | None
    refresh_token: str | None
