import datetime

import jwt
from fastapi import Depends
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session

from Token.token_repository import TokenRepository
from container import Container
from database.database_model import *
from model import *
from fastapi_jwt_auth import AuthJWT

meta = MetaData()
engine = create_engine(Container().db["url"], echo=True)
meta.create_all(engine)
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DatabaseRepository:

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
    def get_person_by_token(access_token: str) -> PersonModel:
        with SessionLocal() as session:
            token = session.query(Token).filter_by(access_token=access_token).one()
            id_person = token.id_person
            refresh_token = token.refresh_token
            person_plus_person_items = session.query(Person).join(PersonItems).filter_by(
                PersonItems.id_person == id_person).all()
            # не дописано

    @staticmethod
    def new_person(p: PersonModel, password: str, refresh_token: str, id_person: str) -> None:
        with SessionLocal() as session:
            session.add(Person(
                id_person=id_person,
                login=p.login,
                id_role=p.role,
                user_password=password
            ))
            session.add(PersonItems(
                id_person=id_person,
                favorite=p.favorite,
                basket=p.basket
            ))
            session.add(Token(
                id_person=id_person,
                refresh_token=refresh_token,
                access_token=p.access_token
            ))
            session.commit()

    @staticmethod
    def get_id_person(token: str) -> str:
        with SessionLocal() as session:
            return session.query(Token).filter_by(refresh_token=token).one().id_person

    @staticmethod
    def get_person_by_login(login: str):
        return (
            SessionLocal()
            .query(Person, PersonItems, Token)
            .join(Token, Person.id_person == Token.id_person)
            .join(PersonItems, Person.id_person == PersonItems.id_person)
            .filter(Person.login == login).first()
        )

    @staticmethod
    def get_all_field(id_person):
        return

    def update_access_token(self, refresh_token: str, new_access_token: str) -> None:
        with SessionLocal() as session:
            id_person = self.get_id_person(refresh_token)
            session.query(Token).filter_by(id_person=id_person).update({
                "access_token": new_access_token
            })
            session.commit()
