# TradeCopilot AI

AI-powered trading assistant that provides real-time market analysis and intelligent buy/sell signals using technical indicators like RSI and MACD.

## Deploy on Render:https://tradecopilot-ai.onrender.com/

##  Features

* Real-time market data (Stocks & Crypto)
*  RSI (Relative Strength Index) indicator
* MACD (Moving Average Convergence Divergence)
* Smart AI-based trading insights
*  FastAPI backend (high performance API)
* Streamlit frontend (interactive UI dashboard)
*  Fallback logic (works without external AI APIs)

## How It Works

1. Fetches real-time data using `yfinance`
2. Calculates RSI & MACD indicators
3. Generates BUY/SELL signals using strategy logic
4. Provides human-like AI explanation based on market conditions
5. Displays results in a clean Streamlit dashboard


## Project Structure

TradeCopilot-AI/
│
├── app/
│   ├── main.py          # FastAPI backend
│   ├── market.py        # Market data + indicators (RSI, MACD)
│   ├── strategy.py      # Trading logic
│   ├── ai_engine.py     # AI-based analysis
│
├── frontend/
│   └── streamlit_app.py # Streamlit UI
│
├── requirements.txt
└── README.md


## Installation & Setup

### Clone the repository

```
git clone https://github.com/kvala8585-crypto/TradeCopilot-AI
cd TradeCopilot-AI
```

### Install dependencies

```
pip install -r requirements.txt
```

---

##  Run the Project Locally

###  Start Backend (FastAPI)

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

###  Start Frontend (Streamlit)

```
streamlit run frontend/streamlit_app.py
```

Open:

```
http://localhost:8501
```

## Deployment

### Backend:

* Deploy on Render using:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

### Frontend:

* Deploy on Streamlit Cloud
* Update API URL in `streamlit_app.py`

---

## Use Cases

* Trading signal assistant
* Learning technical analysis
* AI-based financial insights
* Portfolio projects for AI/ML roles

##  Future Improvements

* Live price charts
*  Chat-based AI assistant
* Telegram / Email alerts

##  Author

kavi vala


