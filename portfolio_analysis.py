import yfinance as yf
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "NVDA", "^GSPC"]

data = yf.download(
    tickers,
    start = "2022-01-01",
    end = "2025-01-01",
    auto_adjust= True
)

prices = data["Close"]

print("Closing Prices: ")
print(prices.head())

returns = prices.pct_change().dropna()
returns_percent = returns * 100
formatted_returns = returns_percent.round(2).astype(str) + "%"
print("\nDaily Returns (%):")
print(formatted_returns.head())

annual_return = returns.mean() * 252
annual_return_percent = annual_return * 100
formatted_annual_return = annual_return_percent.round(2).astype(str) + "%"
print("\nAnnualized Return (%):")
print(formatted_annual_return)

"""
Notes

Nvidia dominates in returns and outperforms microsoft and apple and the market
Indicates high-growth phase
likely drive by AI demand surge in 2022
Generates higher returns but this likely comes with higer volatility and risk

Apple & Microsoft is strong and stable and outperform the market
Apple & Microsoft are more moderate in growth but consistent

S&P 500 = baseline
8% = typical markey benchmark used to compare performance 

"""

volatility = returns.std() * np.sqrt(252)

volatility_percent = volatility * 100
formated_volatility = volatility_percent.round(2).astype(str) + '%'

print("\n Annualized Volatility (%):")
print(formated_volatility)

"""
Nvidia gives extremely hgih returns but its price swings are large
High risk High reward

Apple and Microsoft returns range from 12-15%
Its Volatility is 27%
Strong performers with moderate risk and consistent growth (efficent growth)

The S&P 500 is a stable benchmark delivering lower returns with the least volatility

The tradeoff between rick and return where higher potential gains are assoicated with increased uncertainty

"""
correlation = returns.corr()
print("\nCorrelation Matrix:")
print(correlation)

"""
Apple & Microsoft (0.68) moderately high correlation
They often move in the same direction because both are large tech companies

Nvidia vs Apple/Microsoft moderate correlation
Moves somwhat with tech but also behaves differently due to its AI-driven growth

Stocks vs S&P Strong correlation
All three follow the overall market trend

Even though Nvida has high returns it is still highly correlated with the market
meaning it doe snot provide strong diversification benefits



"""