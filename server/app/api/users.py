from fastapi import FastAPI

from ..db.session import session
from ..models.User import User


def users_api(app: FastAPI):
    @app.get("/users")
    async def get_users():
        users = session.query(User).all()
        return {"users": [user.to_dict() for user in users]}
