import requests
from sqlalchemy.orm import Session
from models import Crypto,Alert, Users
from fastapi import APIRouter
import requests
from sqlalchemy.orm import Session
from models import Crypto, Alert
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc"

router = APIRouter(
    prefix='/updatePrice',
    tags=['updatePrice']
)

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc"

GMAIL_USERNAME = os.getenv('EMAIL_USER')
GMAIL_PASSWORD = os.getenv('EMAIL_PASS')

def send_otp_email(email,crypto):
    subject = "Your Cryto alert has been triggered"
    body = f"Your alert for crypto: {crypto} has been triggered"

    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain'))
    msg['Subject'] = subject
    msg['From'] = str(GMAIL_USERNAME)
    msg['To'] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(str(GMAIL_USERNAME),str(GMAIL_PASSWORD))
        server.sendmail(str(GMAIL_USERNAME), email, msg.as_string())

def update_prices(db: Session):
    print("Control is here at update prices")
    response = requests.get(COINGECKO_URL)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")

    data = response.json()
    for item in data:
        crypto_id = item['id']
        crypto_name = item['name']
        current_price = item['current_price']

        crypto = db.query(Crypto).filter(Crypto.id == crypto_id).first()
        if crypto:
            crypto.price = current_price
        else:
            crypto = Crypto(id=crypto_id, cryptoName=crypto_name, price=current_price)
            db.add(crypto)
    
    db.commit()
    print("Control is checking alerts")
    alerts = db.query(Alert).filter(Alert.isActive == False).all()
    for alert in alerts:
        crypto = db.query(Crypto).filter(Crypto.id == alert.cryptoName).first()
        if crypto and crypto.price > alert.alertPrice:
            print("Check: Alert triggered for", alert.cryptoName)
            user = db.query(Users).filter(Users.username == alert.owner_name).first()
            send_otp_email(user.email,alert.cryptoName)
            alert.isActive = True
            db.add(alert)
    db.commit()