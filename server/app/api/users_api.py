from fastapi import FastAPI
from fastapi import HTTPException

from ..schema.user_schema import UserCreate
from ..db.base import session
from ..models.User_model import User


def users_api(app: FastAPI):
    @app.get("/users")
    async def get_users():
        users = session.query(User).all()
        return {"users": [user.to_dict() for user in users]}

    @app.post('/users')
    async def create_user(user: UserCreate):
        db_user = session.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail='Email already registered')

        new_user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {'username': new_user.username, 'email': new_user.email, 'id': new_user.id}



