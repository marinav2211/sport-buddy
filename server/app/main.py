from .api.users_api import users_api

from .db.base import init_db

from fastapi import FastAPI


app = FastAPI()


def main():
    init_db()
    users_api(app=app)
