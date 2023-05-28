from passlib.context import CryptContext

from database.database_repository import DatabaseRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Password(DatabaseRepository):
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_password(password) -> str:  # хэшится пароль
        return pwd_context.hash(password)
