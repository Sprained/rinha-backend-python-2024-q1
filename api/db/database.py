from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://admin:123@localhost/rinha")
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


class DatabaseUtils:
    @staticmethod
    def get_db():
        """Return session database"""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
