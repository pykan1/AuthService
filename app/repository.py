from typing import Any

from pydantic import BaseModel

from Auth.login_repository import LoginRepository
from Auth.register_repository import RegisterRepository
from Token.token_repository import TokenRepository
from database.database_repository import DatabaseRepository
from model import RegAuthModel, PersonResponse
from password.password_repository import Password


class Repository:
    def __init__(self, **data: Any):
        super().__init__(**data)
        self._registerRepository: RegisterRepository = RegisterRepository()
        self._tokenRepository = TokenRepository()
        self._loginRepository = LoginRepository
        self._databaseRepository = DatabaseRepository()
        self._passwordRepository = Password()

    def person_login(self, user: RegAuthModel):
        ...

    def person_register(self, user: RegAuthModel):
        password = self._passwordRepository.get_password_hash(user.password)
        access_token = self._tokenRepository.create_access_token(user.login)
        refresh_token = self._tokenRepository.create_refresh_token(user.login)
        person = self._registerRepository.register(
            user=user,
            access_token=access_token
        ),
        self._databaseRepository.new_person(
            p=person[0],
            password=password,
            refresh_token=refresh_token
        )
        return person

    def update_access_token(self, refresh_token):
        ...
