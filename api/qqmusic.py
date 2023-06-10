import requests

from tools.headers import get_headers
from tools.jsonxasc import jsonxasc

headers = get_headers()


def listen_time(qq):
    api_url_1 = f'http://api.qdikun.com/api/qqmusic/?qq={qq}'
    api_url_2 = f'https://dachebijia.001api.com/Api/qy?qq={qq}&t=1'

    return [get_url_1(api_url_1), get_url_2(api_url_2)]


def get_url_1(url):
    r = requests.get(url, headers=headers).text
    return r


def get_url_2(url):
    r = requests.get(url, headers=headers).text
    return r
