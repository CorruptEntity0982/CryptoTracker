from fastapi import APIRouter, Depends, HTTPException,status,Path
from typing import Annotated
from sqlalchemy.orm import Session
from models import Crypto,Users,Alert
from database import SessionLocal
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter(
    tags=['Alerts']
)

class AlertRequest(BaseModel):
    alert_id : int = Field(gt=0)
    cryptoName : str = Field(min_length=3, max_length=1000)
    alertPrice : int = Field(gt=0)
    isActive : bool = False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependancy = Annotated[Session,Depends(get_db)]
user_dependancy = Annotated[dict,Depends(get_current_user)]

@router.post("/createAlert", status_code= status.HTTP_201_CREATED)
async def createAlert(user: user_dependancy,
                           request:AlertRequest, 
                           db: db_dependancy):
    
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication failed")
    alert_model = Alert(**request.dict(),owner_name = user.get('username'))
    db.add(alert_model)
    db.commit()


@router.delete("/Alerts/{alert_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_alert(user:user_dependancy,db:db_dependancy,id:int):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication failed")
    
    alert_model = db.query(Alert).filter(Alert.alert_id ==id).first()
    if alert_model is None:
        raise HTTPException(status_code=404, detail="alert not found")
    db.query(Alert).filter(Alert.alert_id == id).delete()
    db.commit()


@router.get("/Alerts/",status_code=status.HTTP_200_OK)
async def read_all_alerts(db: db_dependancy,user: user_dependancy):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication failed")
    return db.query(Alert).filter(Alert.owner_name == user.get('username')).all()

@router.get("/TriggeredAlerts/",status_code=status.HTTP_200_OK)
async def read_all_triggeredAlerts(db: db_dependancy,user: user_dependancy):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication failed")
    return db.query(Alert).filter(Alert.owner_name == user.get('username')).filter(Alert.isActive == True).all()








# @router.put("/todos/{id}",status_code=status.HTTP_204_NO_CONTENT)
# async def update_todo(user:user_dependancy,db:db_dependancy,todo_id:int, request: TodoRequest):
#     if user is None:
#         raise HTTPException(status_code=401,detail="Authentication failed")
    
#     todo_model = db.query(Todos).filter(Todos.id==todo_id)\
#         .filter(Todos.owner_id==user.get('id')).first()
   
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail="Todo not found")
    
#     todo_model.title = request.title
#     todo_model.descp = request.descp
#     todo_model.complete = request.complete
#     todo_model.priority = request.priority
#     db.add(todo_model)
#     db.commit()


