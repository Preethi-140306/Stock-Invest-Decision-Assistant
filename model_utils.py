import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # suppress oneDNN info messages

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Function to calculate RSI
def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# Main function: train LSTM, predict next day, and make investment decision
def train_predict_decide(ticker, start_date, end_date):

    # Download stock data
    df = yf.download(ticker, start=start_date, end=end_date)

    # Require at least 250 data points
    if len(df) < 250:
        return None

    close = df['Close']
    data = close.values.reshape(-1, 1)

    # Scale data for LSTM
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data)

    # Create LSTM sequences
    X, y = [], []
    for i in range(60, len(scaled)):
        X.append(scaled[i-60:i, 0])
        y.append(scaled[i, 0])

    X = np.array(X).reshape(-1, 60, 1)
    y = np.array(y)

    # Build LSTM model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(60,1)),
        Dropout(0.2),
        LSTM(50),
        Dropout(0.2),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")

    # Train model (verbose=0 to not flood console)
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)

    # Predict next day price
    last_60 = scaled[-60:].reshape(1, 60, 1)
    predicted_price = model.predict(last_60, verbose=0)[0][0]
    predicted_price = float(scaler.inverse_transform([[predicted_price]])[0][0])

    # Current price
    current_price = float(close.iloc[-1])

    # Indicators
    ma50 = float(close.rolling(50).mean().iloc[-1])
    ma200 = float(close.rolling(200).mean().iloc[-1])
    rsi_value = float(rsi(close).iloc[-1])

    # Expected return in %
    expected_return = (predicted_price - current_price) / current_price * 100
    expected_return = float(expected_return)

    # Investment decision logic
    if expected_return > 3 and ma50 > ma200 and 40 < rsi_value < 70:
        decision = "🟢 GOOD TO INVEST"
    elif expected_return > 0:
        decision = "🟡 WAIT / HOLD"
    else:
        decision = "🔴 NOT GOOD TO INVEST"

    # Return dictionary with all info
    return {
        "current_price": current_price,
        "predicted_price": predicted_price,
        "expected_return": expected_return,
        "rsi": rsi_value,
        "ma_trend": "Uptrend" if ma50 > ma200 else "Downtrend",
        "decision": decision
    }
