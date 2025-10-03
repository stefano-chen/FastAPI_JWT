from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from common.settings import get_settings

settings = get_settings()

engine = create_engine(url=f"postgresql://{settings.PSQL_USER}:{settings.PSQL_PASSWORD}@{settings.PSQL_HOST}:{settings.PSQL_PORT}/{settings.PSQL_DB}")

def get_db_session():
    with Session(bind=engine) as session:
        try:
            yield session
        finally:
            session.close()