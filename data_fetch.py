# fetch stock data from yahoo finance
import yfinance as yf

def fetch_stock_data():
    global history
    ticker = input("Ticker: ")
    dat = yf.Ticker(ticker)
    history = dat.history(period='6mo')
    return history