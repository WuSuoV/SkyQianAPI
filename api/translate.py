import requests
from urllib3 import disable_warnings

disable_warnings()
from tools import headers


# 有道云翻译接口
def youdao(text):
    url = f"https://fanyi.youdao.com/translate?doctype=json&type=AUTO&i={text}"
    myheaders = headers.get_headers()
    return requests.get(url, headers=myheaders, verify=False).json()
