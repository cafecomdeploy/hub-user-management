from typing import List
from fastapi import APIRouter, Depends, Response, status, Query
from sqlalchemy.orm import Session
from app.schemas.users import Users, UserOutput
from app.controllers.deps import get_db_session
from app.services.users import UsersService
from fastapi_pagination import Page, add_pagination



router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new user")
def add_users(
    user: Users,
    db_session: Session = Depends(get_db_session) # cria uma nova sessao com BD por injecao de dependencia
):
    uc = UsersService(db_session=db_session)
    uc.add_users(user=user)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list', response_model=Page[UserOutput], description="List users")
def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(50, ge=1, le=100, description="Size of page"),
    db_session: Session = Depends(get_db_session)
):
    uc = UsersService(db_session=db_session)
    response = uc.list_users(page=page, size=size)

    return response

@router.delete('/delete/{id}', description="Delete user")
def delete_user(
    id: int,
    db_sesion: Session = Depends(get_db_session)
):
    uc = UsersService(db_session=db_sesion)
    uc.delete_user(id=id)

    return Response(status_code=status.HTTP_200_OK)

@router.put("/update/{item_id}", response_model=Users, description="Change user")
def update_user(
    user: Users,
    db_session: Session = Depends(get_db_session) # cria uma nova sessao com BD por injecao de dependencia
):
    uc = UsersService(db_session=db_session)
    uc.update_users(user=user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
