from fastapi import Depends

from model import *
import uuid


class RegisterRepository(PersonModel):

    def register(self, user: RegModel, access_token, id_person, basket=None, favorite=None) -> PersonModel:
        print(user.number)
        self.get_model(
            id_person=id_person,
            login=user.login,
            id_role=user.id_role,
            access_token=access_token,
            basket=basket,
            favorite=favorite,
            number=user.number
        )
        return self

    @staticmethod
    def create_id():
        id_person = uuid.uuid4()
        return id_person
