from sqlalchemy.orm import Session
from app.models.users import Users as UsersModel 
from app.schemas.users import Users, UserOutput
from fastapi.exceptions import HTTPException
from fastapi import status


class UsersService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_users(self, user: Users):
        user_model = UsersModel(**user.dict())
        self.db_session.add(user_model)
        self.db_session.commit()