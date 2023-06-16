from model import *


class LoginRepository(PersonModel):
    def login_user(self, user: RegAuthModel, access_token, id_person, basket=None, favorite=None, reviews=None, orders=None) -> PersonModel:
        self.get_model(id_person, user.login, user.id_role, access_token, basket, favorite, reviews, orders)
        return self
