from model import RegAuthModel
from repository import Repository


class Service:
    def __init__(self, repository: Repository):
        self._repository = repository

    def register(self, user: RegAuthModel):
        self._repository.person_register(user)


