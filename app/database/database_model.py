from psycopg2.extensions import JSONB
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id_role = Column(Integer, primary_key=True)
    role = Column(String(40), nullable=False)


class Category(Base):
    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True)
    category = Column(String, nullable=False, unique=True)


class Person(Base):
    __tablename__ = 'person'

    id_person = Column(Integer, nullable=False, primary_key=True)
    id_role = Column(Integer, ForeignKey('role.id_role'), nullable=False)
    login = Column(String(20), nullable=False)
    user_password = Column(String(1000), nullable=False)

    role = relationship('Role')


class Token(Base):
    __tablename__ = 'token'

    id_person = Column(Integer, ForeignKey('person.id_person'), primary_key=True, nullable=False)
    access_token = Column(String(1000), nullable=False)
    refresh_token = Column(String(1000), nullable=False)

    person = relationship('Person')


class PersonItems(Base):
    __tablename__ = 'person_items'

    id_person = Column(Integer, ForeignKey('person.id_person'), primary_key=True, nullable=False)
    favorite = Column(Text)
    basket = Column(Text)
    person = relationship('Person')


class Item(Base):
    __tablename__ = 'item'

    id_item = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id_category'), nullable=False)
    name = Column(String(40), nullable=False)
    description = Column(Text)
    reviews = Column(Text)
    amount = Column(Integer, nullable=False)

    category = relationship('Category')
