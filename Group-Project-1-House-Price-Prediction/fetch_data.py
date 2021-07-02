import motor.motor_asyncio
from pprint import pprint
import asyncio
from config import mongo_config
import pandas as pd

client = motor.motor_asyncio.AsyncIOMotorClient()

shards = ",".join(mongo_config["shards"])
client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://{mongo_config["username"]}:{mongo_config["pwd"]}@{shards}?authSource=admin&readPreference=primary&ssl=true')

db = client["house-price-db"]
collection = db["house-price"]


async def do_find_one(collection):
    document = await collection.find_one()
    pprint(document)

async def do_find(collection, n: int):
    cursor = collection.find().limit(n)
    all_docs = []
    async for document in cursor:
        all_docs.append(document)
    return all_docs

loop = asyncio.get_event_loop()
docs = loop.run_until_complete(do_find(collection, 100))
print("\n[INFO] : Data successfully pulled from Atlas DB!\n")

df = pd.DataFrame.from_records(docs)
print(df.shape)