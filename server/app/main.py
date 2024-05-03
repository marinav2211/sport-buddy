from .api.users import users_api
from .db.init_db import init_db

from fastapi import FastAPI


app = FastAPI()


def main():
    init_db()
    users_api(app=app)
