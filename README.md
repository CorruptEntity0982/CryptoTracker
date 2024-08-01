# CryptoTracker

### Application Overview
A price alert application that triggers an email when the user’s target price is
Achieved.
Say, the current price of BTC is 28,000, a user sets an alert for BTC at a price of 33,000.
The application sends an email to the user when the price of BTC reaches 33,000.
Similarly, say, the current price of BTC is 35,000, a user sets an alert for BTC at a price of
33,000. The application should send an email when the price of BTC reaches 33,000.

I've used fastapi(python library for creating these endpoints) along with email STMP services.
Also ive used "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=ma" to get the prices of cryptocurrencies.


### Project setup instructions
kindly run the following command to install all dependencies on your local machine
```
pip install -r requirements.txt
```
Create an .env file with the following information, inside the backend folder.
```
EMAIL_USER = [Your email id] (Used to sent alerts to users on email)
EMAIL_PASS = [App_Password for the gmail account] (Enable 2 factor auth on your google account, after which under security-> App_Passwords, you can create your own app password.)
```
To run the application, cd into Backend folder
```
python3 -m uvicorn main:app --reload
```
Incase "SSH"ing into my database doesnt work, please follow the following steps to set up the database on your local machine,
In the "Database.py" file, edit the following line
```
SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:{your password}@{Host Name}/{Name of your database}'
```

### Video Demonstration
The following url contains an video link demonstrating the project: https://youtu.be/RcJv80AMjko
