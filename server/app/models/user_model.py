from sqlalchemy import Column, Integer, String
from ..mixins.model_mixins import SerializerMixin

from ..db.base import Base


class User(Base, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)


