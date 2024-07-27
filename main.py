from fastapi import FastAPI
import models
from database import engine
from Routers import auth, users, updatePrice, Alerts
from Routers.scheduler import schedule_price_update, scheduler 

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(updatePrice.router)
app.include_router(Alerts.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Crypto API"}

if __name__ == "__main__":
    schedule_price_update()
    scheduler.start()
    print("running")