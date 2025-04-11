# ETL Pipeline for Stock Market Analysis

This project is an automated ETL (Extract, Transform, Load) pipeline that collects, enriches, and stores stock market data using Python. It fetches real-time and historical stock information, news articles, sentiment analysis, and currency exchange rates, and stores the enriched dataset into a MongoDB collection.

---

## 🚀 Features

- Extracts historical stock data from CSV.
- Retrieves real-time stock data using Yahoo Finance.
- Fetches latest news articles via NewsAPI.
- Performs sentiment analysis with Finnhub.
- Converts currency using ExchangeRate API.
- Cleans and transforms data with pandas.
- Stores enriched data into MongoDB.
- Saves final dataset as a CSV.
- Modular and script-based design for scheduling or automation.

---

## 🛠️ Technologies Used

- Python 3
- pandas
- yfinance
- requests
- MongoDB
- Git & GitHub
- GitHub Actions (for CI/CD)
- Scheduler (Python `schedule` module)

---

## 📁 Project Structure

```
project-root/
│
├── config/
│   └── config.json               # Contains API keys
│
├── data/
│   └── historical_data_large.csv
│
├── output/
│   └── final_cleaned_data.csv
│
├── etl_pipeline.py              # Main ETL pipeline
├── load_to_db.py                # MongoDB insert logic
├── requirements.txt             # Python dependencies
├── scheduler.py                 # Schedule daily jobs
├── .github/
│   └── workflows/
│       └── ci_cd.yml            # GitHub Actions config
└── README.md                    # Project overview
```

---

## ▶️ How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Config File**:
   Create a file at `config/config.json`:
   ```json
   {
     "NEWS_API_KEY": "your_newsapi_key",
     "FINNHUB_API_KEY": "your_finnhub_key"
   }
   ```

3. **Run the Pipeline**:
   ```bash
   python etl_pipeline.py
   ```

---

## 📦 Output

- Cleaned data saved in: `output/final_cleaned_data.csv`
- Enriched records inserted into MongoDB collection

---

## 🧪 CI/CD

GitHub Actions is configured to automate testing, deployment, and job scheduling. The CI/CD pipeline ensures:

- ✅ Reduced manual errors
- ✅ Faster feedback during development
- ✅ Automated data integrity checks
- ✅ Reliable deployments

Workflow config: `.github/workflows/ci_cd.yml`

---

## ✅ To-Do / Improvements

- [x] Convert notebook to modular scripts
- [x] Add timezone-aware timestamps
- [x] Use MongoDB as primary storage
- [x] Local execution working via VSCode
- [x] Setup CI/CD with GitHub Actions
- [x] Add automatic scheduling (e.g., with `schedule` or cron)
- [ ] Enable email notifications for scheduler job completion

---

## 👨‍💻 Author

**Abdul Sami**  
Student ID: DS-055  
Course: Big Data Analytics
