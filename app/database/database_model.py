from uuid import UUID

from sqlalchemy import Column, Integer, String, Text, ForeignKey, ARRAY, UUID, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

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

    id_person = Column(UUID, nullable=False, primary_key=True)
    id_role = Column(Integer, ForeignKey('role.id_role'), nullable=False)
    login = Column(String(20), nullable=False)
    user_password = Column(String(1000), nullable=False)

    role = relationship('Role')


class Token(Base):
    __tablename__ = 'token'

    id_person = Column(UUID, ForeignKey('person.id_person'), primary_key=True, nullable=False)
    access_token = Column(String(1000), nullable=False)
    refresh_token = Column(String(1000), nullable=False)

    person = relationship('Person')


class Item(Base):
    __tablename__ = 'item'

    id_item = Column(UUID, primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id_category'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    reviews = Column(Text)
    amount = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=True)
    rate = Column(Float, nullable=True)

    category = relationship('Category')


class PersonItems(Base):
    __tablename__ = 'person_items'

    id_person = Column(UUID, ForeignKey('person.id_person'), primary_key=True, nullable=False)
    favorite = Column(JSONB, nullable=True)
    basket = Column(JSONB, nullable=True)
    reviews = Column(JSONB, nullable=True)
    orders = Column(JSONB, nullable=True)
    person = relationship('Person')
