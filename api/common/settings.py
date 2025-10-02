import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        self.PSQL_USER=os.getenv("PSQL_USER")
        self.PSQL_PASSWORD=os.getenv("PSQL_PASSWORD")
        self.PSQL_HOST=os.getenv("PSQL_HOST")
        self.PSQL_PORT=os.getenv("PSQL_PORT")
        self.PSQL_DB=os.getenv("PSQL_DB")


def get_settings():
    load_dotenv(".env")
    return Settings()
