from Token.token_repository import TokenRepository
from model import *
from database.database_repository import DatabaseRepository
from password.password_repository import Password


class RegisterRepository(PersonResponse):

    def register(self, user: RegAuthModel, access_token, basket=None, favorite=None) -> PersonResponse:
        super().login(user.login)
        super().role(user.id_role)
        super().access_token(access_token)
        super().basket(basket)
        super().favorite(favorite)

        return super()
