from fastapi import FastAPI
from pydantic import BaseModel

from getprice import get_contract_from_symbol, get_price_from_symbol


app = FastAPI()


class InputData(BaseModel):
    network: str
    symbol: str


@app.get("/v1/prodict/")
async def health_check():
    return {
        "status": True,
        "message": "",
        "data": ""
    }, 200


@app.post("/v1/prodict/get_contract_symbol/")
async def get_contract_fromSymbol(data: InputData):

    data = await get_contract_from_symbol(data.network, data.start, data.limit, data.symbol)
    if data is not None:
        return {"status": True, "massage": "", "data": data}, 200
    return {"status": False, "massage": "", "data": ""}, 200


@app.post("/v1/prodict/get_price_symbol/")
async def get_price_fromSymbol(data: InputData):

    data = await get_price_from_symbol(data.network, data.symbol, 1, "USDC")
    if data is not None:
        return {"status": True, "massage": "", "data": data}, 200
    return {"status": False, "massage": "", "data": ""}, 200
