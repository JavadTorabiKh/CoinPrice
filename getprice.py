from utils import request_marketcap_v1
from requests import Request, Session
from config import COINMARKETURL, COINMARKETKEY
from utils import request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_contract_from_symbol(network, symbol):
    network = str(network).lower()
    symbol = str(symbol).upper()

    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': symbol
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETKEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(COINMARKETURL, params=parameters)
        data = json.loads(response.text)
        return data["status"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        raise e


def get_price_from_symbol(network, symbol):

    try:
        data = request_marketcap_v1(
            network, symbol, "v1/tools/price-conversion", 1)
        if data is None:
            raise ConnectionError

        price = float(data["data"]["quote"]["USD"]["price"])
        return {"status": True, "massage": "", "data": price}, 200

    except:
        return {"status": False, "massage": "", "data": None}, 400
