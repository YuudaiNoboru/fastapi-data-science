from fastapi import FastAPI, File

app = FastAPI()

@app.post("/files")
async def update_file(file: bytes = File(...)):
    return {"file_size": len(file)}