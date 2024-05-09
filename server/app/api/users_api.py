from fastapi import FastAPI
from fastapi import APIRouter, HTTPException

from ..schema.user_schema import UserCreate
from ..db.base import session
from ..models.User_model import User
from ..security.security import verify_password, hash_password


def users_api(app: FastAPI):
    router = APIRouter()

    @router.get("/users")
    async def get_users():
        users = session.query(User).all()
        return {"users": [user.to_dict() for user in users]}

    @router.post('/users/register')
    async def register_user(user: UserCreate):
        db_user = session.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail='Email already registered')

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {'username': new_user.username, 'email': new_user.email}

    @router.post('/users/auth')
    async def login_user(user: UserCreate):
        db_user = session.query(User).filter(User.email == user.email).first()
        if not db_user:
            raise HTTPException(status_code=404, detail='User not found.')
        if verify_password(user.password, db_user.password):
            return {'message': 'Login successful', 'username': db_user.username}
        else:
            raise HTTPException(status_code=401, detail='Incorrect password')

    app.include_router(router)


