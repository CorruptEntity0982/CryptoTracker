from fastapi import APIRouter,Depends, HTTPException
from pydantic import BaseModel,Field
from models import Users
from passlib.context import CryptContext
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

SECRET_KEY = '095be1d862deaf5f2f063db0576f1da68da9e9929237a6a959e81f6620754a7d'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username: str
    password: str
    email : str

class Token(BaseModel):
    access_token : str
    token_type : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependancy = Annotated[Session,Depends(get_db)]

def authenticate_user(username:str,password:str,db):
    user = db.query(Users).filter(Users.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

def create_access_token(username:str,expires_delta: timedelta):
    encode = {'sub':username}
    expires = datetime.utcnow()+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,ALGORITHM)

async def get_current_user(token: Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= "Could not validate")
        return {'username': username}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= "Could not validate")

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependancy,
                      create_user_request: CreateUserRequest):
    
    create_user_model = Users(
        username = create_user_request.username,
        hashed_password = bcrypt_context.hash(create_user_request.password),
        email = create_user_request.email,
    ) 
    db.add(create_user_model)
    db.commit()

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependancy):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= "Could not validate")
    token = create_access_token(user.username,timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

