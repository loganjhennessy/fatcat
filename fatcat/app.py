from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StockModel(BaseModel):
    symbol: str
    bigFive: bool
    stickerPrice: float
    currentPrice: float


@app.get("/")
async def root():
    return "Use /api to get a valid response"


@app.get("/api", response_model=List[StockModel])
async def get_stock_list():
    return [{
        "symbol": "DAL",
        "bigFive": True,
        "stickerPrice": 45.00,
        "currentPrice": 29.00
    }]
