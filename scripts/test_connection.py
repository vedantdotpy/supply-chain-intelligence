import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()


DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


connection_string = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(connection_string)


try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print(result.fetchone())

    print("Database connection successful!")

except Exception as e:
    print("Connection failed:")
    print(e)