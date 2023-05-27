from pydantic import BaseModel
from middleware import Middleware
from model import RegAuthModel
from repository import Repository
import time


class Service:
    middleware = Middleware()

    def __init__(self, repository: Repository):
        self._repository = repository

    @middleware.handler_login
    def register(self, user: RegAuthModel):
        return self._repository.person_register(user)

    @middleware.handler_password
    def login(self, user: RegAuthModel):
        return self._repository.person_login(user)

    def update_access_token(self, refresh_token):
        return self._repository.update_access_token(refresh_token)
