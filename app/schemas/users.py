import re
from pydantic import validator
from pydantic import BaseModel
from datetime import datetime


class Users(BaseModel):
    firstname: str
    lastname: str
    date: datetime

# Utilizando regex para realizar validacao do firstname
    @validator('firstname')
    def validate_firstname(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid firstname')
        return value

class UserOutput(Users):
    id: int