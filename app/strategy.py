def generate_signal(price, high, low, rsi, macd, macd_signal):
    
    # 🔥 Strong signals (RSI + MACD combo)
    if rsi < 30 and macd > macd_signal:
        return "STRONG BUY (RSI + MACD)"

    elif rsi > 70 and macd < macd_signal:
        return "STRONG SELL (RSI + MACD)"

    # 🔹 RSI based signals
    elif rsi < 30:
        return "BUY (Oversold - RSI)"

    elif rsi > 70:
        return "SELL (Overbought - RSI)"

    # 🔹 MACD crossover
    elif macd > macd_signal:
        return "BUY (MACD Bullish)"

    elif macd < macd_signal:
        return "SELL (MACD Bearish)"

    # 🔹 Support / Resistance fallback (tamaro original logic)
    elif price > (high * 0.98):
        return "SELL (near resistance)"

    elif price < (low * 1.02):
        return "BUY (near support)"

    else:
        return "HOLD"