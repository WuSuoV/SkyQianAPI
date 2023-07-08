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
    res = {2: '正常，未被拦截', 1: '显示非官方页面', 0: '警告！已被拦截', -1: '未知错误'}
    num = detect_domain(url)
    if num != -1:
        return {
            'code': 200,
            'url': url,
            'msg': res[num]
        }
    else:
        return {
            'code': 500,
            'msg': res[num]
        }