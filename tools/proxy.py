import random
from config import myconfig


def get_proxies():
    with open(file=myconfig.get('rootpath') + '/http_proxies.txt', mode='r',
              encoding='utf8') as f:
        txt = f.read()
    proxies = txt.split('\n')
    new_proxies = []
    for i in proxies:
        new_proxies.append({'http': 'http://' + i, 'https': 'http://' + i})
    return new_proxies


def random_proxy():
    return random.choice(get_proxies())


# clash代理
def local_proxy():
    return {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
