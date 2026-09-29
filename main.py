from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATA_FILE = Path(__file__).parent / "data.txt"

app = FastAPI(title="Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/api/data")
def save_data(msg: Message):
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(msg.text + "\n")
    return {"status": "ok"}

@app.get("/api/data")
def read_data():
    if not DATA_FILE.exists():
        return {"content": ""}
    return {"content": DATA_FILE.read_text(encoding="utf-8")}
