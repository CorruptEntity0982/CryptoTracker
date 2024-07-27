# CryptoTracker

##Introduction

Hi, My name is Shashank Dubey, A computer science and engineering student from Vellore Institute of Technology, your company tanX.fi has recently come to my university for college placements. After going through the Job description, the role you're offering aligns with my interests, however i'm not able to apply through my university for this role as I have a standing backlog (Due to oversight in my answer script, re-evaluation of my test in in progress and I will clear the backlog by Decemeber 2024). 

I have attempted the backend assignment that was part of the mail i've received.
Problem Statement:

Application Overview
Create a price alert application that triggers an email when the user’s target price is
Achieved.
Say, the current price of BTC is $28,000, a user sets an alert for BTC at a price of 33,000$.
The application should send an email to the user when the price of BTC reaches 33,000$.
Similarly, say, the current price of BTC is 35,000$, a user sets an alert for BTC at a price of
33,000$. The application should send an email when the price of BTC reaches 33,000$.

I've used fastapi(python library for creating these endpoints) along with email STMP services.
Also ive used "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=ma" to get the prices of cryptocurrencies as Binance has a pay wall.

The following url contains an video link demonstrating the project.
