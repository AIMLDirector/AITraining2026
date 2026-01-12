import yfinance as yf
import pandas as pd

def get_trend_metrics(ticker):
    """
    Input: ticker (e.g., "INFY.NS")
    Output: dict with YTD return, 50d and 200d SMA trend, last price
    """

    # Fetch 1 year data
    df = yf.Ticker(ticker).history(period="1y", interval="1d")

    if df.empty:
        return None

    # Latest price
    last_price = df["Close"].iloc[-1]

    # YTD return = (last - first-of-year) / first-of-year
    ytd_return = (last_price - df["Close"].iloc[0]) / df["Close"].iloc[0] * 100

    # Simple moving averages
    sma_50 = df["Close"].rolling(50).mean().iloc[-1]
    sma_200 = df["Close"].rolling(200).mean().iloc[-1]

    # Trend signal
    trend = "Uptrend" if sma_50 > sma_200 else "Downtrend"

    return {
        "last_price": last_price,
        "ytd_return_pct": round(ytd_return, 2),
        "sma_50": round(sma_50, 2),
        "sma_200": round(sma_200, 2),
        "trend": trend
    }
