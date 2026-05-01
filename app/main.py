from fastapi import FastAPI
from app.market import get_stock_data
from app.strategy import generate_signal
from app.ai_engine import get_ai_analysis

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TradeCopilot AI running"}

@app.get("/analyze")
def analyze(symbol: str = "BTC-USD"):
    data = get_stock_data(symbol)

    if not data:
        return {"error": "No data"}

    # 🔥 Updated: RSI + MACD pass kariye
    signal = generate_signal(
        data["price"],
        data["high"],
        data["low"],
        data["rsi"],
        data["macd"],
        data["macd_signal"]
    )

    ai_text = get_ai_analysis(data, signal)

    return {
        "symbol": symbol,
        "data": data,
        "signal": signal,
        "ai_analysis": ai_text
    }