from fastapi import FastAPI
from app.controllers.users import router as category_routes



app = FastAPI()
@app.get('/')
def health_check():
    return True

app.include_router(category_routes)