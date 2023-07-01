from pydantic import BaseModel
from sqlalchemy.orm import Session

from middleware import Middleware
from model import *
from repository import Repository


class Service:
    middleware = Middleware()

    def __init__(self, repository: Repository):
        self._repository = repository

    @middleware.handler_register
    def register(self, user: RegModel, db: Session):
        return self._repository.person_register(user, db)

    @middleware.handler_login
    def login(self, user: AuthModel, person: PersonResponse, db: Session):
        return self._repository.person_login(user=user, person=person, db=db)

    def update_access_token(self, refresh_token, db: Session):
        return self._repository.update_access_token(refresh_token, db)

    def check_number(self, db: Session, number: str):
        return self._repository.check_person_number(db, number)
