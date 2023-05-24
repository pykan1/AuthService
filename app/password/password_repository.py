from passlib.context import CryptContext

from database.database_repository import DatabaseRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Password(DatabaseRepository):
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):  # хэшится пароль
        return pwd_context.hash(password)

    def create_password(self, login, password: str) -> str:
        ...

    def authenticate_user(self, login: str, password: str):
        user = self.get_person_by_login(login)
        if not user:
            return False
        if not self.verify_password(password, user.user_password):
            return False
        return user

