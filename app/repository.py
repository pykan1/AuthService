from Auth.register_repository import RegisterRepository
from database.database_repository import DatabaseRepository
from model import RegAuthModel


class Repository(RegisterRepository, DatabaseRepository):
    def person_login(self, user: RegAuthModel):
        ...

    def person_register(self, user: RegAuthModel):
        self.register(user)

    def update_access_token(self, refresh_token):
        ...
