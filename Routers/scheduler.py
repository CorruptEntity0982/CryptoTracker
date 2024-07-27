from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .updatePrice import update_prices
from database import SessionLocal

scheduler = BackgroundScheduler()

def schedule_price_update():
    def update():
        db = SessionLocal()
        try:
            update_prices(db)
        finally:
            db.close()
    scheduler.add_job(update, IntervalTrigger(minutes=1))


