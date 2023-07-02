from model import *


class LoginRepository(PersonModel):
    def login_user(self, user: AuthModel, login: str, access_token, refresh_token,  id_person, basket=None, favorite=None, reviews=None,
                   orders=None) -> PersonModel:
        self.get_model(id_person, login, user.id_role, access_token, refresh_token, basket, favorite, reviews, orders,
                       user.number)
        return self
