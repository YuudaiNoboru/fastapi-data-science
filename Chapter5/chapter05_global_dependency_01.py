from fastapi import Header, HTTPException, status, FastAPI, Depends, APIRouter

def secret_header(secret_header: str | None = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

app = FastAPI(dependencies=[Depends(secret_header)])

@app.get("/route1")
async def router_route1():
    return {"route": "router1"}

@app.get("/route2")
async def router_route2():
    return {"route": "router2"}