import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load environment variables
load_dotenv()


# Database configuration
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# Create database engine

if DB_HOST is None:
    DB_HOST = "localhost"


connection_string = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(connection_string)

print("Database engine initialized")