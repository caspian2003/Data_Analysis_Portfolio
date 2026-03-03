# 📊 Financial Data Analysis Portfolio

A professional **financial portfolio analysis tool** built using Python and Jupyter Notebook. This project analyzes stocks, indices, cryptocurrencies, forex, and commodities to generate insights, visualizations, and risk metrics.

---

## 🔹 Project Overview

The goal of this project is to create a **complete data analysis portfolio** focusing on the finance domain.  
It provides end-to-end analysis including:

- Portfolio returns and correlations
- Candlestick charts for individual assets
- Portfolio risk metrics (volatility, Sharpe ratio)
- PnL calculations
- Interactive charts for insights
- Automated download of real-time market data

This portfolio is suitable for **finance internships, data analysis projects, or professional reporting**.

---

## 🛠️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/financial-data-portfolio.git
cd financial-data-portfolio

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Open Jupyter Notebook
jupyter notebook

Open finance_portfolio.ipynb and run all cells sequentially.

💻 Code Structure
financial-data-portfolio/
├── finance_portfolio.ipynb       # Main Jupyter Notebook
├── requirements.txt              # Python dependencies
├── visualizations/
│   └── charts/                   # PNG & HTML charts are saved here
├── datasets/                      # Optional dataset storage
├── reports/                       # Exported PDF or summary reports
├── docs/                          # Detailed project documentation
└── README.md

Notebook contains all analysis: returns, heatmap, candlestick, portfolio metrics.

📊 Features / Visual Documentation

Returns Chart: Interactive line chart of portfolio returns

Correlation Heatmap: Shows relationship between all assets

Candlestick Charts: Daily OHLC charts for each stock, crypto, forex, and commodity

Portfolio Analytics: Annualized return, volatility, Sharpe ratio, PnL

File Storage: All charts are timestamped to prevent overwriting

Sample Screenshot (replace with your own):


⚙️ Technical Details

Languages & Libraries: Python 3, Pandas, Numpy, Matplotlib, Seaborn, Plotly, mplfinance, yfinance

Data Sources: Yahoo Finance API via yfinance

Algorithms & Metrics:

Daily returns: pct_change()

Portfolio return & volatility: np.dot(weights, returns.mean())

Sharpe Ratio: return / volatility

PnL: Latest price vs purchase price

Visualization: Matplotlib / Seaborn for static charts, Plotly for interactive charts, mplfinance for candlesticks

🧪 Testing Evidence

Tested with multiple asset classes: Nifty 50, Bank Nifty, US stocks, top crypto, Forex, Commodities

Output files verified: All returns, heatmaps, and candlestick PNGs and HTMLs saved with timestamps

Validation: Checked calculations for portfolio metrics against sample manual calculations

📂 Usage

Open finance_portfolio.ipynb

Select desired symbols or use default pre-defined assets

Run all cells

Charts & portfolio metrics are generated automatically in visualizations/charts/

📜 Recommendations

Extend portfolio with custom weights per asset

Use longer periods for historical analysis

Add forecasting models for predictive insights (optional)
