# 📊 Smart Stock Risk Analyzer

This project uses Python and machine learning to help beginner investors make more informed stock decisions. It predicts whether a stock is likely to **go up**, **go down**, or **stay flat** over the next few days based on technical indicators.

---

## 🔍 Features

- Fetches 6 months of historical stock data from Yahoo Finance
- Calculates:
  - 7-day Moving Average
  - 14-day Volatility
  - 14-day RSI (Relative Strength Index)
- Trains a machine learning model (Random Forest) to predict short-term trends
- Displays the prediction and latest indicators in a clean **Streamlit dashboard**
- Works with any stock ticker (e.g., AAPL, TSLA, AMD)

---

pip install -r requirements.txt
streamlit run dashboard.py
OR
https://lucamenastockriskanalyzer.streamlit.app

## 🛠️ Potential Improvements
- Add fundamental analysis (e.g., P/E ratio, revenue growth, debt levels)
- Let users compare multiple stocks side-by-side
- Display risk scores or “investment health” grades
- Save predictions and track model accuracy over time
- Add support for multi-day trend forecasting

## Uses
python, streamlit, scikit-learn, yfinance, pandas, matplotlib

enjoy