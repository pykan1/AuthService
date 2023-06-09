from sqlalchemy.orm import Session

from Auth.login_repository import LoginRepository
from Auth.register_repository import RegisterRepository
from Token.token_repository import TokenRepository
from database.database_model import Person
from database.database_repository import DatabaseRepository
from model import *
from password.password_repository import Password


class Repository:

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._registerRepository: RegisterRepository = RegisterRepository()
        self._tokenRepository = TokenRepository()
        self._loginRepository = LoginRepository()
        self._databaseRepository = DatabaseRepository()
        self._passwordRepository = Password()
        self._personResponse = PersonModel()

    def person_login(self, user: AuthModel, person, db: Session):
        # person - кортеж из 3 объектов таблица Person, PersonItems, Token
        new_access_token = self._tokenRepository.create_access_token(
            login=person[0].login,
            id_role=person[0].id_role,
            uuid=str(person[0].id_person)
        )

        self._databaseRepository.update_access_token(
            refresh_token=person[2].refresh_token,
            new_access_token=new_access_token,
            db=db
        )

        self._personResponse = self._loginRepository.login_user(
            user=user,
            login=person[0].login,
            access_token=new_access_token,
            id_person=person[0].id_person,
            basket=person[1].basket,
            favorite=person[1].favorite,
            reviews=person[1].reviews,
            orders=person[1].reviews,
            refresh_token=person[2].refresh_token
        )

        return self._personResponse

    def person_register(self, user: RegModel, db: Session):
        id_person = self._registerRepository.create_id()
        password = self._passwordRepository.create_password(user.password)
        access_token = self._tokenRepository.create_access_token(
            login=user.login,
            id_role=user.id_role,
            uuid=str(id_person)
        )

        self._personResponse = self._registerRepository.register(
            user=user,
            id_person=id_person,
            access_token=access_token,
            refresh_token=self._tokenRepository.create_refresh_token(
                login=user.login,
                id_role=user.id_role,
                uuid=str(id_person)
            )
        )

        self._databaseRepository.new_person(
            id_person=id_person,
            p=self._personResponse,
            password=password,
            db=db
        )

        return self._personResponse

    def update_access_token(self, refresh_token, db: Session) -> str:
        data = self._tokenRepository.get_token_data(refresh_token)
        new_access_token = self._tokenRepository.create_access_token(
            login=data["sub"],
            id_role=data["id_role"],
            uuid=data["uuid"]
        )

        self._databaseRepository.update_access_token(
            refresh_token=refresh_token,
            new_access_token=new_access_token,
            db=db
        )
        return new_access_token

    @staticmethod
    def check_person_number(db: Session, number: str) -> bool:
        query = db.query(Person).filter_by(number=number).all()
        print(f"ааааа {query}  {type(query)}")
        if not query:
            return False
        return True
