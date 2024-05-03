from sqlalchemy import create_engine
from ..core.config import connection_string

engine = create_engine(connection_string)
