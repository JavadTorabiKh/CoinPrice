from fastapi import FastAPI
from pydantic import BaseModel

from getprice import get_contract_from_symbol, get_price_from_symbol


app = FastAPI()


class InputData(BaseModel):
    network: str
    symbol: str


@app.get("/")
async def health_check():
    return {
        "status": True,
        "message": "",
        "data": ""
    }


@app.post("/get_price_symbol/")
async def get_price_fromSymbol(data: InputData):

    data = await get_price_from_symbol(data.network, data.symbol, 1, "USDC")
    return res
