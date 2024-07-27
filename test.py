import requests
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc"
response = requests.get(COINGECKO_URL)
print(response.status_code, response.json())
