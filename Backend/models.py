from Backend.database import Base
from sqlalchemy import Column, Integer,String,Boolean, ForeignKey

class Crypto(Base):
    __tablename__ = 'crypto'
    id = Column(String, primary_key=True, index=True)
    cryptoName  = Column(String)
    price = Column(Integer)

class Users(Base):
    __tablename__ = "users"
    username = Column(String,primary_key=True,index=True)
    hashed_password = Column(String)
    email = Column(String)

class Alert(Base):
    __tablename__ = 'alerts'
    alert_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cryptoName = Column(String)
    alertPrice =  Column(Integer)
    isActive = Column(Boolean)
    owner_name = Column(String, ForeignKey("users.username"))
    
