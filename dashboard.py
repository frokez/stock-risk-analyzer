#optional
# for streamlit dashboard version
from indicators import MA7, volatility, getRSI
from model import label_trend, prepare_data, train_model, predict_today
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
st.set_page_config(page_title="Smart Stock Analyzer", layout="centered")
st.title("📊 Smart Stock Risk Analyzer📊")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):")

def fetch_data(ticker):
    global history
    dat = yf.Ticker(ticker)
    history = dat.history(period='6mo')
    return history
if ticker:
    global history
    history = fetch_data(ticker) # get pd dataframe
    MA7(history) # get moving average of 7 days
    volatility(history) # get volatility
    getRSI(history) # get rsi
    label_trend(history) # label up down flat
    X_train, X_test, y_train, y_test=prepare_data(history) # split into variables
    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    prediction = predict_today(model, history)
    st.subheader("📈 Model Prediction")
    st.write(f"📊 Predicted trend: **{prediction[0]}**")
    latest = history[['MA_7', 'volatility_14d', 'RSI']].iloc[-1]
    st.subheader("📊 Technical Indicators (Latest)")
    st.write(f"7-Day Moving Average: {latest['MA_7']:.2f}")
    st.write(f"14-Day Volatility: {latest['volatility_14d']:.4f}")
    st.write(f"RSI: {latest['RSI']:.2f}")
    st.subheader("📉 Price vs Moving Average")
    fig, ax = plt.subplots()
    history['Close'].plot(ax=ax, label="Close")
    history['MA_7'].plot(ax=ax, label="7-Day MA")
    ax.legend()
    st.pyplot(fig)



