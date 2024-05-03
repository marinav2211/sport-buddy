from .engine import engine
from .base import Base


def init_db():
    Base.metadata.create_all(engine)
