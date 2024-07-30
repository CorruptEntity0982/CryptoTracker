from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:try12345@localhost/CryptoTracker'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()