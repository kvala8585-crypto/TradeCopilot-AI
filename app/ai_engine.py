def get_ai_analysis(data, signal):
    price = round(data["price"], 2)
    high = round(data["high"], 2)
    low = round(data["low"], 2)
    rsi = round(data["rsi"], 2)

    # 🔥 Price position detection (NEW)
    if abs(price - high) < (0.002 * price):
        position = "very close to resistance"
    elif abs(price - low) < (0.002 * price):
        position = "very close to support"
    else:
        position = "in the middle range"

    # 🔥 Strong signals
    if "STRONG BUY" in signal:
        return f"Strong BUY signal. Price is {price}, {position}. RSI is {rsi}, indicating oversold conditions. Momentum is bullish — consider buying."

    elif "STRONG SELL" in signal:
        return f"Strong SELL signal. Price is {price}, {position}. RSI is {rsi}, indicating overbought conditions. Momentum is bearish — consider selling."

    # 🔹 Normal signals
    elif "BUY" in signal:
        return f"Price is {price}, {position}. RSI is {rsi}. Market may move upward — consider buying with proper risk management."

    elif "SELL" in signal:
        return f"Price is {price}, {position}. RSI is {rsi}. Market may reverse — consider selling or booking profit."

    else:
        return f"Price is {price}, {position}. RSI is {rsi}. Market is sideways between {low} and {high}. Better to wait for a clear trend."