from sqlalchemy import Column, Integer, String

from ..db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)


