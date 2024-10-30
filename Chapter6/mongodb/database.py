from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

motor_client:AsyncIOMotorClient = AsyncIOMotorClient("localhost", 27017)

database = motor_client["chapter06_mongo"]

def get_databese() -> AsyncIOMotorDatabase:
    return database