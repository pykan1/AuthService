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
        id_person = self._registerRepository.create_id()
        password = self._passwordRepository.create_password(user.password)
        access_token = self._tokenRepository.create_access_token(user.login)
        refresh_token = self._tokenRepository.create_refresh_token(user.login)
        person = self._registerRepository.register(
            user=user,
            id_person=id_person,
            access_token=access_token
        )
        self._databaseRepository.new_person(
            id_person=id_person,
            p=person,
            password=password,
            refresh_token=refresh_token
        )
        return person

    def update_access_token(self, refresh_token) -> str:
        login = self._tokenRepository.get_login(refresh_token)
        new_access_token = self._tokenRepository.create_access_token(login)
        self._databaseRepository.update_access_token(
            refresh_token=refresh_token,
            new_access_token=new_access_token
        )
        return new_access_token
