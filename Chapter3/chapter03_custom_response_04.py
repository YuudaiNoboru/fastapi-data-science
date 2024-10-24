from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get("/cat")
async def get_cat():
    root_directory = Path(__file__).parent.parent
    picture_patch = root_directory/"Chapter3"/"assets"/"cat.jpg"
    return FileResponse(picture_patch)