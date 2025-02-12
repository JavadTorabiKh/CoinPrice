from requests import Session
import json
from config import COINMARKETURL, COINMARKETKEY
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def request_marketcap_v1(network, root, parameters):

    network = str(network).lower()
    symbol = str(symbol).upper()

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETKEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(
            COINMARKETURL+root, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return None
