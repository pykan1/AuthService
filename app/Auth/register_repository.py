from fastapi import Depends

from Token.token_repository import TokenRepository
from model import *
from database.database_repository import DatabaseRepository
from password.password_repository import Password


class RegisterRepository(PersonResponse):

    def register(self, user: RegAuthModel, access_token, basket=None, favorite=None) -> PersonResponse:
        self.get_model(user.login, user.id_role, access_token, basket, favorite)
        print(self.__dict__)
        return self
