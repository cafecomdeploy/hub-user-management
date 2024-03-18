from fastapi import status, Response, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.controllers.deps import get_db_session
from app.schemas.login import Login
from app.services.login import LoginService


router = APIRouter(prefix='/login')

@router.post('/registra')
def login_register(
    login: Login,
    db_session: Session = Depends(get_db_session)
):
    uc = LoginService(db_session=db_session)
    uc.register_login(login=login)
    return Response(status_code=status.HTTP_201_CREATED)


@router.post('/autenticacao')
def user_login(
    login_request_form: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session)
):
    uc = LoginService(db_session=db_session)

    login = Login(
        username=login_request_form.username,
        password=login_request_form.password
    )

    token_data = uc.login(login=login, expires_in=60)

    return token_data