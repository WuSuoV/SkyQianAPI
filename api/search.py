import requests
from urllib3 import disable_warnings

disable_warnings()
from tools import headers, proxy

myheaders = headers.get_headers()


def search_from_1ovebbs(keyword):
    url = f"https://bbs.1ove.club/search-{keyword}.htm?ajax=1"
    r = requests.get(url, headers=myheaders, verify=False, proxies=proxy.local_proxy()).json()
    return [{'name': str(i.get('subject')).replace('<span class="text-danger">', '').replace('</span>', ''),
             'url': 'https://bbs.1ove.club/' + i.get('url')} for i in r.get('message')]


if __name__ == '__main__':
    print(search_from_1ovebbs('我的'))
