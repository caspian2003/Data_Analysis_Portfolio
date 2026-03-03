import streamlit as st
import pandas as pd
import yfinance as yf
import mplfinance as mpf # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os

st.title(" Financial Market Analysis Dashboard")

st.write("Stocks | Crypto | Forex | Commodities")

# Assets
assets = {
"Apple": "AAPL",
"Tesla": "TSLA",
"Microsoft": "MSFT",
"Reliance": "RELIANCE.NS",
"Infosys": "INFY.NS",
"Bitcoin": "BTC-USD",
"Ethereum": "ETH-USD",
"Gold": "GC=F",
"Silver": "SI=F",
"EUR/USD": "EURUSD=X",
"USD/INR": "USDINR=X"
}

asset = st.selectbox("Select Asset", list(assets.keys()))

symbol = assets[asset]

period = st.selectbox(
"Select Period",
["1mo","3mo","6mo","1y","2y"]
)

data = yf.download(symbol, period=period)

st.subheader("Price Data")

st.write(data.tail())

# Price chart
st.subheader("Price Trend")

fig, ax = plt.subplots()

data["Close"].plot(ax=ax)

st.pyplot(fig)

# Returns
returns = data["Close"].pct_change().dropna()

st.subheader("Returns")

fig2, ax2 = plt.subplots()

returns.plot(ax=ax2)

st.pyplot(fig2)

# Candlestick
st.subheader("Candlestick Chart")

mpf_fig, mpf_ax = mpf.plot(
    data,
    type="candle",
    style="yahoo",
    volume=True,
    returnfig=True
)

st.pyplot(mpf_fig)

# Volatility
volatility = returns.std()

st.subheader("Volatility")

st.write(volatility)

st.success("Dashboard Loaded Successfully")