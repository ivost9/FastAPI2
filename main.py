from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/sum")
def calculate_sum(data: Numbers):
    return {"sum": data.a + data.b}

app.mount("/static", StaticFiles(directory="static"), name="static")