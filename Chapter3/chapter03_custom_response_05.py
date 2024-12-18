from fastapi import FastAPI
from fastapi.responses import Response
from pathlib import Path

app = FastAPI()

@app.get("/xml")
async def get_xml():
    content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="aplication/xml")