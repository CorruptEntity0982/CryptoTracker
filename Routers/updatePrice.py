from fastapi import HTTPException
from sqlalchemy.orm import Session
import requests
from models import Crypto
from fastapi import APIRouter,Depends, HTTPException



router = APIRouter(
    prefix='/updatePrice',
    tags=['updatePrice']
)

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc"

def update_prices(db: Session):
    response = requests.get(COINGECKO_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from CoinGecko")

    data = response.json()
    for item in data:
        crypto = db.query(Crypto).filter(Crypto.id == item['id']).first()
        if crypto:
            crypto.price = item['current_price']
        else:
            crypto = Crypto(
                id=item['id'],
                cryptoName=item['name'],
                price=item['current_price']
            )
            db.add(crypto)
    
    db.commit()
