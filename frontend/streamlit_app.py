import streamlit as st
import requests

st.title("📈 TradeCopilot AI")

symbol = st.text_input("Enter Symbol (e.g. BTC-USD)", "BTC-USD")

if st.button("Analyze"):
    res = requests.get(f"http://localhost:8000/analyze?symbol={symbol}")
    data = res.json()

    if "error" in data:
        st.error(data["error"])
    else:
        # 🔥 Price (NEW ADD)
        st.write("### 💰 Current Price")
        st.success(round(data["data"]["price"], 2))

        # 🔥 Signal
        st.write("### 📊 Signal")
        st.success(data["signal"])

        # 🔥 Market Indicators
        st.write("### 📈 Market Indicators")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("RSI", round(data["data"]["rsi"], 2))

        with col2:
            st.metric("MACD", round(data["data"]["macd"], 2))

        with col3:
            st.metric("MACD Signal", round(data["data"]["macd_signal"], 2))

        # 🔥 AI Analysis
        st.write("### 🤖 AI Analysis")
        st.info(data["ai_analysis"])