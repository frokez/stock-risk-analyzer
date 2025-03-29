# calculate technical indicators

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