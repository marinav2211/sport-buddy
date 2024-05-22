from dotenv import load_dotenv
import os
from sqlalchemy import URL

load_dotenv()


connection_string = URL.create(
    drivername='postgresql+asyncpg',
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    database='neondb',
)
