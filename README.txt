ETL Pipeline for Stock Market Analysis
======================================

This project is an automated ETL (Extract, Transform, Load) pipeline that collects, enriches, and stores stock market data using Python. It fetches real-time and historical stock information, news articles, sentiment analysis, and currency exchange rates, and stores the enriched dataset into a MongoDB collection.

--------------------------------------------------------------
Features
--------------------------------------------------------------
- Extracts historical stock data from CSV.
- Retrieves real-time stock data using Yahoo Finance.
- Fetches latest news articles via NewsAPI.
- Performs sentiment analysis with Finnhub.
- Converts currency using ExchangeRate API.
- Cleans and transforms data with pandas.
- Stores enriched data into MongoDB.
- Saves final dataset as a CSV.
- Modular and script-based design for scheduling or automation.

--------------------------------------------------------------
Technologies Used
--------------------------------------------------------------
- Python 3
- pandas
- yfinance
- requests
- MongoDB
- Git & GitHub
- GitHub Actions (for CI/CD)
- Scheduler support (optional automation)

--------------------------------------------------------------
Project Structure
--------------------------------------------------------------
project-root/
│
├── config/
│   └── config.json         -> Contains API keys
│
├── data/
│   └── historical_data_large.csv
│
├── output/
│   └── final_cleaned_data.csv
│
├── etl_pipeline.py         -> Main ETL pipeline
├── load_to_db.py           -> MongoDB insert logic
├── requirements.txt        -> Python dependencies
└── README.txt              -> Project overview

--------------------------------------------------------------
How to Run
--------------------------------------------------------------
1. Install Dependencies:
   pip install -r requirements.txt

2. Set Up Config File:
   Inside config/config.json:
   {
     "NEWS_API_KEY": "your_newsapi_key",
     "FINNHUB_API_KEY": "your_finnhub_key"
   }

3. Run the Pipeline:
   python etl_pipeline.py

--------------------------------------------------------------
Output
--------------------------------------------------------------
- Cleaned data saved in: output/final_cleaned_data.csv
- Enriched records inserted into MongoDB collection

--------------------------------------------------------------
To-Do / Improvements
--------------------------------------------------------------
[x] Convert notebook to modular scripts
[x] Add timezone-aware timestamps
[x] Use MongoDB as primary storage
[x] Local execution working via VSCode
[ ] Setup CI/CD with GitHub Actions
[ ] Add automatic scheduling (e.g., with 'schedule' or cron)

--------------------------------------------------------------
Author
--------------------------------------------------------------
Abdul Sami  
Student ID: DS-055  
Course: Big Data Analytics
