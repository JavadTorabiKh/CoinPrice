import requests


def request(path, timeout, method='GET', headers=None, payload=None):
    try:
        if method.lower() == 'get':
            res = requests.get(url=path, headers=headers,
                               timeout=timeout, data=payload)
        elif method.lower() == 'post':
            res = requests.post(url=path, headers=headers,
                                timeout=timeout, data=payload)
        else:
            raise Exception
        if res.status_code == 200:
            return res.json()
        else:
            raise Exception
    except:
        raise ConnectionError
