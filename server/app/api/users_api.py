from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, Depends

from ..schema.user_schema import UserCreate
from ..db.base import AsyncSessionLocal, get_db
from ..models.user_model import User
from ..security.security import verify_password, hash_password


def users_api(app: FastAPI):
    router = APIRouter()

    @router.get("/users")
    async def get_users(db: AsyncSessionLocal = Depends(get_db)):
        result = await db.execte(select(User))
        users = result.scalars().all()
        return {"users": [user.to_dict() for user in users]}

    @router.post('/users/register')
    async def register_user(user: UserCreate, db: AsyncSessionLocal = Depends(get_db)):
        result = await db.execte(select(User).filter(User.email == user.email))
        db_user = result.scalars().first()
        if db_user:
            raise HTTPException(status_code=400, detail='Email already registered')

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return {'username': new_user.username, 'email': new_user.email}

    @router.post('/users/auth')
    async def login_user(user: UserCreate, db: AsyncSessionLocal = Depends(get_db)):
        result = await db.execte(select(User).filter(User.email == user.email))
        db_user = result.scalars().first()
        if not db_user:
            raise HTTPException(status_code=404, detail='User not found.')
        if verify_password(user.password, db_user.password):
            return {'message': 'Login successful', 'username': db_user.username}
        else:
            raise HTTPException(status_code=401, detail='Incorrect password')

    app.include_router(router)


