from requests import Request, Session
from config import COINMARKETURL, COINMARKETKEY
from utils import request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_price_from_symbol(network, symbol):
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
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        raise e


a = get_price_from_symbol("bitcoin", "usd")
print(a)
