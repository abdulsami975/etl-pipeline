import schedule
import time
from etl_pipeline import etl_job

schedule.every().day.at("14:29").do(etl_job)

print("⏱️ ETL Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)
