# CryptoTracker

## Introduction

Hi, My name is Shashank Dubey, A computer science and engineering student from Vellore Institute of Technology, your company tanX.fi has recently come to my university for college placements. After going through the Job description, the role you're offering aligns with my interests, however i'm not able to apply through my university for this role as I have a standing backlog (Due to oversight in my answer script, re-evaluation of my test is in progress and I will clear the backlog by Decemeber 2024). 
I have attempted the backend assignment that was part of the mail i've received.


### Application Overview
Create a price alert application that triggers an email when the user’s target price is
Achieved.
Say, the current price of BTC is 28,000, a user sets an alert for BTC at a price of 33,000.
The application should send an email to the user when the price of BTC reaches 33,000.
Similarly, say, the current price of BTC is 35,000, a user sets an alert for BTC at a price of
33,000. The application should send an email when the price of BTC reaches 33,000.

I've used fastapi(python library for creating these endpoints) along with email STMP services.
Also ive used "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=ma" to get the prices of cryptocurrencies as "Binance.com" has a pay wall to generate an api-key.

### Contact me
Kindly contact me at shashank02.dubey@gmail.com should you be interest in pursing me as a candidate for this role.
Attached is my resume: https://drive.google.com/file/d/1Ps5l05m9Ypwu_z1dXZ0JZclRzVixXeTL/view?usp=share_link
LinkedIn: https://www.linkedin.com/in/shashank-dubey-b3684a21b/
Please dont report me to the university officials :)

### Project setup instructions
kindly run the following command to install all dependencies on your local machine
```
pip install -r requirements.txt
```
To run the application
```
python3 -m uvicorn main:app --reload
```
Incase "SSH"ing into my database doesnt work, please follow the following steps to set up the database on your local machine,
In the "Database.py" file, edit the following line
```
SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:{your password}@{Host Name}/{Name of your database}'
```

### Video Demonstration
The following url contains an video link demonstrating the project: 
