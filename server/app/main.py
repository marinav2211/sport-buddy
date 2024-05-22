
from .api.users_api import users_api
from .api.event_api import event_api

from .db.base import init_db

from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def main():
    print('HELLO')

    await init_db()
    users_api(app=app)
    event_api(app=app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
