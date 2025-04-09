from pymongo import MongoClient
import json

with open("config/config.json") as f:
    config = json.load(f)

def insert_to_mongo(data):
    client = MongoClient(config["MONGO_URI"])
    db = client['etl_pipeline_data']
    collection = db['financial_data']
    collection.insert_many(data)
    print(f"📥 Inserted {len(data)} records into MongoDB")
