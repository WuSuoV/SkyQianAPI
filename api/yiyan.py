import requests
from urllib3 import disable_warnings

disable_warnings()
from tools import headers


def yiyan():
    return requests.get('https://international.v1.hitokoto.cn/?c=d&encoding=json&charset=utf-8', verify=False,
                        headers=headers.get_headers()).json()


if __name__ == '__main__':
    print(yiyan())
