import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from data_fetch import fetch_stock_data
from indicators import MA7, volatility, getRSI
from model import label_trend, prepare_data, predict_today, train_model




def main():
    global history
    history = fetch_stock_data() # get pd dataframe
    MA7(history) # get moving average of 7 days
    volatility(history) # get volatility
    getRSI(history) # get rsi
    label_trend(history) # label up down flat
    X_train, X_test, y_train, y_test=prepare_data(history) # split into variables
    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(predict_today(model,history))


main()