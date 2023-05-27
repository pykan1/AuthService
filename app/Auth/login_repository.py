from model import *


class LoginRepository(PersonModel):
    def login_user(self, user: RegAuthModel, access_token, id_person, basket=None, favorite=None) -> PersonModel:
        self.get_model(id_person, user.login, user.id_role, access_token, basket, favorite)
        return self
