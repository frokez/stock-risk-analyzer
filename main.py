#entry point for cli or app
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report




def fetch_stock_data():
    global history
    ticker = input("Ticker: ")
    dat = yf.Ticker(ticker)
    history = dat.history(period='6mo')
    return history
def MA7(history):
    history['MA_7'] = history['Close'].rolling(window=7).mean()
    last_ma_7 = history['MA_7'].iloc[-1]
    return last_ma_7

def volatility(history):
    history['daily_return'] = history['Close'].pct_change()
    history['volatility_14d'] = history['daily_return'].rolling(window=14).std()

def getRSI(history):
    history['Difference'] = history['Close'].diff()
    history['Gain'] = history['Difference'].apply(lambda x: x if x > 0 else 0)
    history['Loss'] = history['Difference'].apply(lambda x: -x if x < 0 else 0)

    avg_gain = history['Gain'].rolling(window=14).mean()
    avg_loss = history['Loss'].rolling(window=14).mean()

    RS = avg_gain / avg_loss
    history['RSI'] = 100 - (100 / (1 + RS))
    
def label_trend(history):
    history['Future_Close'] = history['Close'].shift(-7)
    history['Future_Return'] = (history['Future_Close'] - history['Close']) / history['Close']

    def classify_return(r):
        if r >= 0.003:
            return "Up"
        elif r <= -0.003:
            return "Down"
        else:
            return "Flat"

    history['Label'] = history['Future_Return'].apply(classify_return)


def prepare_data(history):
    history.dropna(inplace=True) # remove NaN
    X = history[['MA_7', 'volatility_14d', 'RSI']] # select these of my x
    y = history['Label'] # these for y
    return train_test_split(X, y, test_size=0.2, random_state=42) # split data

def predict_today(model):
    lastrow = history.tail(1)
    X = lastrow[['MA_7', 'volatility_14d', 'RSI']]
    return model.predict(X)

def main():
    history = fetch_stock_data() # get pd dataframe
    MA7(history) # get moving average of 7 days
    volatility(history) # get volatility
    getRSI(history) # get rsi
    label_trend(history) # label up down flat
    X_train, X_test, y_train, y_test=prepare_data(history) # split into variables
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(predict_today(model))


main()