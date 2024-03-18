from decouple import config
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from app.schemas.login import Login, TokenData
from app.models.models import Login as LoginModel

crypt_context = CryptContext(schemes=['sha256_crypt'])

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

class LoginService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def register_login(self, login: Login):
        login_on_db = LoginModel(
            username=login.username,
            password=crypt_context.hash(login.password)
        )

        self.db_session.add(login_on_db)

        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username existente!')

    def login(self, login: Login, expires_in: int = 30):
        login_on_db = self._get_user(username=login.username)

        if login_on_db is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Username ou senha não existe!')

        if not crypt_context.verify(login.password, login_on_db.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Username ou senha não existe!')
        
        expires_at = datetime.utcnow() + timedelta(expires_in)

        data = {
            'sub': login_on_db.username,
            'exp': expires_at
        }

        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        token_data = TokenData(access_token=access_token, expires_at=expires_at)
        return token_data

    def verify_token(self, token: str):
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Inválido')
        
        login_on_db = self._get_user(username=data['sub'])

        if login_on_db is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Inválido')

    def _get_user(self, username: str):
        login_on_db = self.db_session.query(LoginModel).filter_by(username=username).first()
        return login_on_db