from fastapi import APIRouter, Depends, HTTPException,status,Path
from typing import Annotated
from sqlalchemy.orm import Session 
from models import Users
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext
from pydantic import BaseModel,Field

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session,Depends(get_db)]
user_dependancy = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

@router.get('/info',status_code=status.HTTP_200_OK)
async def get_user_information(user:user_dependancy,db:db_dependancy):
    if user is None:
        raise HTTPException(status_code=401,detail="Authorisation Failed")
    user_model = db.query(Users).filter(Users.username == user.get('username')).first()
    if user_model is None:
        raise HTTPException(status_code=404,detail="User not found")
    return {user_model}

@router.post('/update_password',status_code=status.HTTP_204_NO_CONTENT)
async def update_user_information(user:user_dependancy,db:db_dependancy,
                                  user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401,detail="Authorisation Failed")
    user_model = db.query(Users).filter(Users.username == user.get('username')).first()
    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()

    
