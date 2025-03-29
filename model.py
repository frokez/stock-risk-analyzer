# train & use ML model for trend prediction
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

global history

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

def predict_today(model,history):
    lastrow = history.tail(1)
    X = lastrow[['MA_7', 'volatility_14d', 'RSI']]
    return model.predict(X)

from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
