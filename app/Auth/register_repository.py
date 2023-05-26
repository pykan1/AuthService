from fastapi import Depends

from Token.token_repository import TokenRepository
from model import *
import uuid


class RegisterRepository(PersonResponse):

    def register(self, user: RegAuthModel, access_token, id_person, basket=None, favorite=None) -> PersonResponse:
        self.get_model(id_person, user.login, user.id_role, access_token, basket, favorite)
        return self

    @staticmethod
    def create_id():
        id_person = uuid.uuid4()
        return id_person
