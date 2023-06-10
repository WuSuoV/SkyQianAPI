import requests
from urllib3 import disable_warnings
disable_warnings()
from tools import headers

def short(url):
    myheaders = headers.get_headers()
    api_url = f"https://dwz.ma/api.php?url={url}"
    res = requests.get(url=api_url, verify=False, headers=myheaders)
    res.encoding = 'utf-8-sig'
    return res.json()


if __name__ == '__main__':
    url = "https://bbs.1ove.club"
    print(short(url))
