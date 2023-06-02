import datetime
import os
import time
from typing import Any

from pydantic import BaseModel

from app.Auth.login_repository import LoginRepository
from app.Auth.register_repository import RegisterRepository
from app.Token.token_repository import TokenRepository
from app.database.database_repository import DatabaseRepository
from app.model import *
from app.password.password_repository import Password


class Repository:

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._registerRepository: RegisterRepository = RegisterRepository()
        self._tokenRepository = TokenRepository()
        self._loginRepository = LoginRepository()
        self._databaseRepository = DatabaseRepository()
        self._passwordRepository = Password()
        self._personResponse = PersonResponse()

    def person_login(self, user: RegAuthModel, person):
        # person - кортеж из 3 объектов таблица Person, PersonItems, Token
        new_access_token = self._tokenRepository.create_access_token(user.login)

        self._databaseRepository.update_access_token(
            refresh_token=person[2].refresh_token,
            new_access_token=new_access_token
        )

        self._personResponse.refresh_token = person[2].refresh_token

        self._personResponse.person = self._loginRepository.login_user(
            user=user,
            access_token=new_access_token,
            id_person=person[0].id_person,
            basket=person[1].basket,
            favorite=person[1].favorite
        )

        return self._personResponse

    def person_register(self, user: RegAuthModel):
        id_person = self._registerRepository.create_id()
        password = self._passwordRepository.create_password(user.password)
        access_token = self._tokenRepository.create_access_token(user.login)

        self._personResponse.refresh_token = self._tokenRepository.create_refresh_token(user.login)
        self._personResponse.person = self._registerRepository.register(
            user=user,
            id_person=id_person,
            access_token=access_token
        )

        self._databaseRepository.new_person(
            id_person=id_person,
            p=self._personResponse.person,
            password=password,
            refresh_token=self._personResponse.refresh_token
        )

        return self._personResponse

    def update_access_token(self, refresh_token) -> str:
        login = self._tokenRepository.get_login(refresh_token)
        new_access_token = self._tokenRepository.create_access_token(login)

        self._databaseRepository.update_access_token(
            refresh_token=refresh_token,
            new_access_token=new_access_token
        )

        return new_access_token
