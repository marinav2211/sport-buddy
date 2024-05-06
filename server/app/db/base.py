from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from ..core.config import connection_string

from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    Base.metadata.create_all(engine)
