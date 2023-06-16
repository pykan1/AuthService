from pydantic import BaseModel
from sqlalchemy.orm import Session

from middleware import Middleware
from model import *
from repository import Repository
import time


class Service:
    middleware = Middleware()

    def __init__(self, repository: Repository):
        self._repository = repository

    @middleware.handler_login
    def register(self, user: RegAuthModel, db: Session):
        return self._repository.person_register(user, db)

    @middleware.handler_register
    def login(self, user: RegAuthModel, person: PersonResponse, db: Session):
        return self._repository.person_login(user=user, person=person, db=db)

    def update_access_token(self, refresh_token, db: Session):
        return self._repository.update_access_token(refresh_token, db)
