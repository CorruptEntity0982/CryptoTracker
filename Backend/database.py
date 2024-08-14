from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

SQL_ALCHEMY_DATABASE_URL = os.getenv("SQL_ALCHEMY_DATABASE_URL")
print(SQL_ALCHEMY_DATABASE_URL)
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()