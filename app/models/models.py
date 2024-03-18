from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    firstname = Column('firstname', String, nullable=False)
    lastname = Column('lastname', String, nullable=False)
    date = Column('date', DateTime, nullable=False) 

class Login(Base):
    __tablename__ = 'realizaLogin'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False)
    password = Column('password', String, nullable=False)