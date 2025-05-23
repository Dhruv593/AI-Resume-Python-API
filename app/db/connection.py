# -*- coding: utf-8 -*-
from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import settings

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def connect_to_mongo():
    try:
        db.client = AsyncIOMotorClient(settings.MONGO_URI)
        db.db = db.client[settings.DB_NAME]
        # Test the connection
        await db.client.admin.command('ping')
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        raise

async def close_mongo_connection():
    if db.client:
        db.client.close() 