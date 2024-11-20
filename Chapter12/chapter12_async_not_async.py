import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/fast")
async def fast():
    return {"endpoint": "fast"}

@app.get("/slow-async")
async def slow_async():
    """Executa no processo principal"""
    time.sleep(10)
    return {"endpoint": "slow-async"}

@app.get("/slow-sync")
def slow_sync():
    """Executando e uma thread"""
    time.sleep(10)
    return {"endpoint": "slow-sync"}