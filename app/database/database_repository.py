import datetime

import jwt
from fastapi import Depends
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session
from container import Container
from database.database_model import *
from model import *
from fastapi_jwt_auth import AuthJWT

meta = MetaData()
engine = create_engine(Container().db["url"], echo=True)
meta.create_all(engine)
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Database:

    @staticmethod
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def get_db_model(db_model: Base, db: Session = Depends(get_db)):
        db = db.query(db_model).all()
        return db

    @staticmethod
    def get_person(access_token: str) -> PersonResponse:
        with SessionLocal() as session:
            token = session.query(Token).filter_by(access_token=access_token).one()
            id_person = token.id_person
            refresh_token = token.refresh_token
            person_plus_person_items = session.query(Person).join(PersonItems).filter(
                Person.id_person == id_person).all()
            # не дописано

    @staticmethod
    def new_person(p: PersonRequest) -> None:
        with SessionLocal() as session:
            session.add(Person(
                login=p.login,
                id_role=p.role,
                user_password=p.password
            ))
            session.add(PersonItems(
                favorite=p.favorite,
                basket=p.basket
            ))
            session.add(Token(
                refresh_token=p.refresh_token,
                access_token=p.access_token
            ))
            session.commit()

    @staticmethod
    def get_login(token: str) -> str:
        return jwt.decode(
            jwt=token,
            key=Container().auth["secret_key"],
            algorithms=["HS256"]
        )["sub"]

    def get_id_person(self, access_token: str) -> int:
        with SessionLocal() as session:
            login = self.get_login(access_token)
            return session.query(Person).filter_by(login=login).one().id_person

    def update_items(self, i: Items) -> None:
        with SessionLocal() as session:
            # id_person = session.query(Person).filter_by(access_token=p.access_token).one().id_person
            id_person = self.get_id_person(i.access_token)
            session.query(PersonItems).filter_by(id_person=id_person).update(
                {"basket": i.basket,
                 "favorite": i.favorite}
            )
            session.commit()

    def update_access_token(self, refresh_token: str, Authorize: AuthJWT = Depends()) -> None:
        with SessionLocal() as session:
            expires = datetime.timedelta(days=3)
            id_person = self.get_id_person(refresh_token)
            login = self.get_login(refresh_token)
            new_access_token = Authorize.create_access_token(subject=login, expires_time=expires)
            session.query(Token).filter_by(id_person=id_person).update({
                "access_token": new_access_token
            })
            session.commit()
