from database.database_repository import DatabaseRepository
from fastapi import HTTPException


class Middleware:
    def __init__(self):
        self._databaseRepository: DatabaseRepository = DatabaseRepository()

    def handler_login(self, function):
        def output(*args):
            person = self._databaseRepository.get_person_by_login(args[1].login)
            if person:
                raise HTTPException(status_code=420, detail="this login is busy")
            else:
                return function(args[0], args[1])

        return output


