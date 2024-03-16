from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.users import Users as UsersModel 

from utils.log import Log
from schemas.users import Users

logger = Log.get_logger(__name__)

class UsersRepository():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def post_users(self, user: Users):
        logger.debug('Adicionando user: {} '.format(str(user)))
        user_model = UsersModel(**user.dict())
        self.db_session.add(user_model)
        self.db_session.commit()
        
    def get_users(self):
        logger.debug('Listando usuários')
        users_on_db = self.db_session.query(UsersModel)