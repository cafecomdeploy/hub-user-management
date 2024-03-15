from typing import List
from fastapi import APIRouter, Depends, Response, status, Query
from sqlalchemy.orm import Session
from app.schemas.users import Users
from app.controllers.deps import get_db_session
from app.services.users import UsersService



router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new user")
def add_users(
    user: Users,
    db_session: Session = Depends(get_db_session) # cria uma nova sessao com BD por injecao de dependencia
):
    uc = UsersService(db_session=db_session)
    uc.add_users(user=user)
    return Response(status_code=status.HTTP_201_CREATED)
