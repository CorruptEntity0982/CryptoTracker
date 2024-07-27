import requests
from sqlalchemy.orm import Session
from models import Crypto
from fastapi import APIRouter, Depends, HTTPException,status,Path 

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc"

router = APIRouter(
    prefix='/updatePrice',
    tags=['updatePrice']
)

def update_prices(db: Session):
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
