from utils import request_marketcap_v1
from requests.exceptions import ConnectionError


def get_contract_from_symbol(network, start, limit, symbol):

    parameters = {
        'start': start,
        'limit': limit,
        'convert': symbol
    }
    try:
        data = request_marketcap_v1(
            network, "", parameters)
        contract = data["contract"]
        return contract
    except:
        return None


async def get_price_from_symbol(network, symbol, amount, convert):

    parameters = {
        'amount': amount,
        "symbol": symbol,
        'convert': convert
    }
    try:
        data = await request_marketcap_v1(
            network, "v1/tools/price-conversion", parameters)
        if data is None:
            raise ConnectionError

        price = float(data["data"]["quote"]["USD"]["price"])
        return price

    except:
        return None
