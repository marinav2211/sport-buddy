from fastapi import FastAPI

from sqlalchemy import URL, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

app = FastAPI()

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def to_dict(self):
        return {"name": self.name, "age": self.age}


connection_string = URL.create(
  'postgresql',
  username='marinochka2288',
  password='7QfTEXqW0Pvb',
  host='ep-cold-wood-42073061.us-east-2.aws.neon.tech',
  database='neondb',
)

engine = create_engine(connection_string)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


@app.get("/users")
async def get_users():
    users = session.query(User).all()
    return {"users": [user.to_dict() for user in users]}

