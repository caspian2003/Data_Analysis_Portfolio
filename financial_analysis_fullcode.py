import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
import plotly.express as px
import plotly.graph_objects as go
import datetime
import os

# Create folders
os.makedirs("visualizations/charts", exist_ok=True)

# ===============================
# USER INPUT
# ===============================
symbols = input("Enter symbols (comma separated, e.g., TSLA,AAPL,BTC-USD): ").upper().split(",")
period = input("Enter period (1mo,3mo,6mo,1y,5y): ")
interval = "1d"

# ===============================
# DOWNLOAD DATA
# ===============================
data = yf.download(symbols, period=period, interval=interval)
close = data["Close"]

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("\nDownloaded Data:")
display(close.tail())

# ===============================
# RETURNS CALCULATION
# ===============================
returns = close.pct_change().dropna()

# ===============================
# RETURNS CHART (Plotly)
# ===============================
fig_returns = px.line(returns, title="Returns Chart")
returns_file = f"visualizations/charts/returns_{timestamp}.html"
fig_returns.write_html(returns_file)
fig_returns.show()
print("Interactive Returns chart saved:", returns_file)

# ===============================
# CORRELATION HEATMAP (Plotly)
# ===============================
corr = returns.corr()
fig_heatmap = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r", title="Correlation Heatmap")
heatmap_file = f"visualizations/charts/heatmap_{timestamp}.html"
fig_heatmap.write_html(heatmap_file)
fig_heatmap.show()
print("Interactive Heatmap saved:", heatmap_file)

# ===============================
# CANDLESTICK CHARTS
# ===============================
for symbol in symbols:
    df = yf.download(symbol, period="3mo", interval="1d")
    df = df[['Open','High','Low','Close','Volume']]
    for col in ['Open','High','Low','Close','Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    
    candle_file = f"visualizations/charts/candlestick_{symbol}_{timestamp}.png"
    mpf.plot(df, type="candle", style="yahoo", volume=True, title=f"{symbol} Candlestick", savefig=candle_file)
    print(f"Candlestick saved: {candle_file}")

# ===============================
# PORTFOLIO RISK & PnL CALCULATOR
# ===============================
# User inputs weights and buy prices
weights = []
buy_prices = []
for s in symbols:
    w = float(input(f"Enter weight of {s} in portfolio (0-1): "))
    weights.append(w)
    p = float(input(f"Enter your buy price for {s}: "))
    buy_prices.append(p)

weights = np.array(weights)
buy_prices = np.array(buy_prices)

# Portfolio return and variance
mean_returns = returns.mean()
cov_matrix = returns.cov()

portfolio_return = np.dot(weights, mean_returns) * 252  # annualized
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix*252, weights)))  # annualized
sharpe_ratio = portfolio_return / portfolio_volatility

# Current PnL
latest_prices = close.iloc[-1].values
pnl = (latest_prices - buy_prices) * weights.sum()  # simplified for demonstration

print("\nPortfolio Analysis:")
print(f"Annualized Return: {portfolio_return:.2%}")
print(f"Annualized Volatility: {portfolio_volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"PnL based on current prices: {pnl}")