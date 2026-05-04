import yfinance as yf
import pandas as pd

def get_stock_data(symbol="BTC-USD"):
    data = yf.download(symbol, period="1d", interval="5m")

    if data.empty:
        return None

    #  RSI Calculation
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    # MACD Calculation
    exp1 = data["Close"].ewm(span=12, adjust=False).mean()
    exp2 = data["Close"].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=9, adjust=False).mean()

    latest = data.iloc[-1]

    return {
        "price": float(latest["Close"]),
        "high": float(latest["High"]),
        "low": float(latest["Low"]),
        "rsi": float(rsi.iloc[-1]),
        "macd": float(macd.iloc[-1]),
        "macd_signal": float(signal_line.iloc[-1])
    }
