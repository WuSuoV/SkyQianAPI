import requests
from urllib3 import disable_warnings

disable_warnings()

myreq = requests.session()
myreq.keep_alive = False


def get_location(domain):
    header = myreq.get(f'https://mp.weixinbridge.com/mp/wapredirect?url={domain}', allow_redirects=False,
                       verify=False).headers
    return dict(header).get('Location')


def detect_domain(url):
    location = get_location(url)
    if location == url:
        # 代表未拦截
        return 2
    else:
        res = myreq.get(location, verify=False).text
        if '已停止访问该网页' in res:
            return 0
        elif '非微信官方网页' in res:
            return 1
        else:
            return -1


def get_res(url):
    res = {2: 'Not blocked', 1: 'Unofficial page', 0: 'Blocked', -1: 'Unknown error'}
    num = detect_domain(url)
    return {'code': num, 'result': res[num]}


