from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def headers(user_agent: str = Header(...)):
    return {"user_agent": user_agent}