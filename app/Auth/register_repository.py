from Token.token_repository import TokenRepository
from model import *
from database.database_repository import DatabaseRepository
from password.password_repository import Password


class RegisterRepository(PersonResponse, TokenRepository, DatabaseRepository, Password):

    def register(self, user: RegAuthModel) -> PersonResponse:
        access_token = self.create_access_token(user.login)
        refresh_token = self.create_refresh_token(user.login)
        password = self.get_password_hash(user.password)

        self.__init__(
            login=user.login,
            role=user.id_role,
            favorite=None,
            basket=None,
            access_token=access_token,
        )

        self.new_person(
            p=self,
            password=password,
            refresh_token=refresh_token
        )

        return self
