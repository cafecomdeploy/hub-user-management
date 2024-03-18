from fastapi import FastAPI
from app.controllers.users import router as user_routes
from app.controllers.login import router as login_routes



app = FastAPI()
@app.get('/')
def health_check():
    return True

app.include_router(user_routes)
app.include_router(login_routes)