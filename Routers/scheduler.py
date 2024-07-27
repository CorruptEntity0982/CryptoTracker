from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from database import SessionLocal
from .updatePrice import update_prices

scheduler = BackgroundScheduler()

def schedule_price_update():
    db = SessionLocal()
    try:
        print("Starting price update")
        update_prices(db)
        print("Price update completed")
    except Exception as e:
        print(f"Error during price update: {e}")
    finally:
        db.close()
    scheduler.add_job(schedule_price_update, IntervalTrigger(minutes=1))
    print("Job scheduled")

if __name__ == "__main__":
    schedule_price_update()
    scheduler.start()
