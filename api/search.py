import requests
from urllib3 import disable_warnings

disable_warnings()
from tools import headers

myheaders = headers.get_headers()


def search_from_1ovebbs(keyword):
    url = f"https://bbs.1ove.club/search-{keyword}.htm?ajax=1"
    r = requests.get(url, headers=myheaders, verify=False).json()
    return [{'name': str(i.get('subject')).replace('<span class="text-danger">', '').replace('</span>', ''),
             'url': 'https://bbs.1ove.club/' + i.get('url')} for i in r.get('message')]
