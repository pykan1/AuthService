from database.database_repository import DatabaseRepository
from fastapi import HTTPException

from password.password_repository import Password


class Middleware:
    def __init__(self):
        self._databaseRepository: DatabaseRepository = DatabaseRepository()
        self._passwordRepository: Password = Password()

    def handler_register(self, function):
        def output(*args):
            person = self._databaseRepository.get_person_by_login(args[1].login, args[2])
            if person:
                raise HTTPException(status_code=420, detail="this login is busy")
            else:
                return function(*args)
        return output

    def handler_login(self, function):
        def output(*args):
            person = self._databaseRepository.get_person_by_number(args[1].number, args[2])
            if not person:
                raise HTTPException(status_code=419, detail="account not found")
            if not self._passwordRepository.verify_password(args[1].password, person[0].user_password):
                raise HTTPException(status_code=420, detail="wrong password")
            else:
                return function(args[0], args[1], person, args[2])
        return output
