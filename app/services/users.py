from sqlalchemy.orm import Session
from app.models.models import Users as UsersModel 
from app.schemas.users import Users, UserOutput
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate

class UsersService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_users(self, user: Users):
        user_model = UsersModel(**user.dict())
        self.db_session.add(user_model)
        self.db_session.commit()
        
    def list_users(self, page: int = 1, size: int = 50):
        users_on_db = self.db_session.query(UsersModel)
        params = Params(page=page, size=size)
        return paginate(users_on_db, params=params)
    
    def delete_user(self, id: int):
        user_model = self.db_session.query(UsersModel).filter_by(id=id).first()
        if not user_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado!')
        
        self.db_session.delete(user_model)
        self.db_session.commit()

    def update_users(self, user: Users):
        user_model =  self.db_session.query(user).filter_by(id=id).first()
        if user_model is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario não encontrado.')
        
        user_model.firstname  = user.firstname
        user_model.lastname = user.lastname
        user_model.date = user.date

        self.db_session.add(user_model)
        self.db_session.commit()






        user_model = UsersModel(**user.dict())
        self.db_session._update_impl(user_model)
        self.db_session.commit()