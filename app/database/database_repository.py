from fastapi import Depends
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session

from container import Container
from database.database_model import *
from model import *

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
            person_plus_person_items = session.query(Person).join(PersonItems).filter(Person.id_person == id_person).all()
            # не дописано

    @staticmethod
    def new_person(p: PersonRequest) -> None:
        with SessionLocal() as session:
            session.add(Person(
                login=p.login,
                
            ))





