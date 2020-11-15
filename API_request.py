from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_price(url, parameters, headers):
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        info = json.loads(response.text)
        return info['data'][0]['quote']['USD']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
