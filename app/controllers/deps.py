from decouple import config
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.connection import Session

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()