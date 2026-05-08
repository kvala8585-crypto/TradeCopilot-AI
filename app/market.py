import yfinance as yf
import pandas as pd

def get_stock_data(symbol="BTC-USD"):

    try:
        # Download stock/crypto data
        data = yf.download(
            symbol,
            period="1d",
            interval="5m",
            progress=False,
            auto_adjust=True
        )

        # Check empty data
        if data.empty:
            return None

        # Convert columns to single values
        close_prices = data["Close"].squeeze()
        high_prices = data["High"].squeeze()
        low_prices = data["Low"].squeeze()

        # ================= RSI =================
        delta = close_prices.diff()

        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # ================= MACD =================
        exp1 = close_prices.ewm(span=12, adjust=False).mean()
        exp2 = close_prices.ewm(span=26, adjust=False).mean()

        macd = exp1 - exp2
        signal_line = macd.ewm(span=9, adjust=False).mean()

        # Latest values
        latest_price = close_prices.iloc[-1]
        latest_high = high_prices.iloc[-1]
        latest_low = low_prices.iloc[-1]

        latest_rsi = rsi.iloc[-1]
        latest_macd = macd.iloc[-1]
        latest_signal = signal_line.iloc[-1]

        return {
            "price": round(float(latest_price), 2),
            "high": round(float(latest_high), 2),
            "low": round(float(latest_low), 2),
            "rsi": round(float(latest_rsi), 2),
            "macd": round(float(latest_macd), 2),
            "macd_signal": round(float(latest_signal), 2)
        }

    except Exception as e:
        print("MARKET DATA ERROR:", e)
        return None
