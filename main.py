from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from typing import List
import shutil
from pathlib import Path

app = FastAPI()

RECEIVED_DIR = Path("received")
RECEIVED_DIR.mkdir(exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h2>RelayX</h2>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="files" multiple required>
                <br><br>
                <button type="submit">Send to Mac</button>
            </form>
        </body>
    </html>
    """

@app.post("/upload")
def upload_files(files: List[UploadFile] = File(...)):
    saved = []
    for file in files:
        destination = RECEIVED_DIR / file.filename
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved.append(file.filename)
    return {"status": "success", "filenames": saved}