from fastapi import FastAPI
from api import router

app = FastAPI()
app.include_router(router)

from db import init_db

init_db()  # Call on startup