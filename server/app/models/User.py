from sqlalchemy import Column, Integer, String

from ..db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def to_dict(self):
        return {"name": self.name, "age": self.age}