from datetime import datetime, timezone
import pandas as pd
import yfinance as yf
import requests
import json
from load_to_db import insert_to_mongo

# Load secrets
with open("config/config.json") as f:
    config = json.load(f)

NEWS_API_KEY = config["NEWS_API_KEY"]
FINNHUB_API_KEY = config["FINNHUB_API_KEY"]

# Load CSV
df_csv = pd.read_csv("data/historical_data_large.csv")

# Helper APIs
def get_yfinance_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        latest = stock.history(period="1d").tail(1)
        if not latest.empty:
            return {
                'latest_price': latest['Close'].values[0],
                'volume': int(latest['Volume'].values[0])
            }
    except:
        return {}
    return {}

def get_stock_news(symbol):
    try:
        url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={NEWS_API_KEY}"
        articles = requests.get(url).json().get("articles", [])
        return articles[:3]
    except:
        return []

def get_sentiment(symbol):
    try:
        url = f"https://finnhub.io/api/v1/news-sentiment?symbol={symbol}&token={FINNHUB_API_KEY}"
        data = requests.get(url).json()
        return {
            'sentiment_score': data.get('sentiment_score', 0),
            'positive': data.get('positive'),
            'negative': data.get('negative'),
            'neutral': data.get('neutral'),
        }
    except:
        return {}

def get_usd_to_inr():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=INR"
        return requests.get(url).json()['rates']['INR']
    except:
        return None

# ETL Job
def etl_job():
    print("🚀 ETL Job running...")
    df_sample = df_csv.head(100)
    enriched_data = []
    usd_to_inr = get_usd_to_inr()

    for _, row in df_sample.iterrows():
        symbol = row['Symbol']
        live = get_yfinance_data(symbol)
        news = get_stock_news(symbol)
        sentiment = get_sentiment(symbol)

        try:
            impact_score = abs(live.get('latest_price', 0) - row.get('Open', 0)) / row.get('Open', 1)
        except ZeroDivisionError:
            impact_score = 0

        enriched_data.append({
            'symbol': symbol,
            'date': row.get('Date', str(datetime.now(timezone.utc))),
            'open': row.get('Open'),
            'close': row.get('Close'),
            'volume_csv': row.get('Volume'),
            'latest_price': live.get('latest_price'),
            'live_volume': live.get('volume'),
            'usd_to_inr': usd_to_inr,
            'sentiment': sentiment,
            'news': news,
            'impact_score': impact_score,
            'timestamp': datetime.now(timezone.utc).isoformat()
        })

    df_final = pd.DataFrame(enriched_data)
    df_final.to_csv("output/final_cleaned_data.csv", index=False)

    # Store in MongoDB
    insert_to_mongo(df_final.to_dict("records"))
    print("✅ ETL complete & data stored!")

# Test mode
if __name__ == "__main__":
    etl_job()