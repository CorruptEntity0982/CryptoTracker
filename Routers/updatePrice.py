from fastapi import APIRouter, Depends, HTTPException,status,Path
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter(
    tags=['updateUser']
)