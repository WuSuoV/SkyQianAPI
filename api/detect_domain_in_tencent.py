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


if __name__ == '__main__':
    res = get_res('https://www.yiove.com')
    print(res)

# 违禁：https://weixin110.qq.com/cgi-bin/mmspamsupport-bin/newredirectconfirmcgi?click=c3a6812fe88abf8cb4ea191ea3ee0cfc&bankey=9ebac403fb028500bb753a8319a8a038&midpagecode=56a2466b749b7f0be6d0e17374747d091192d20ac181a7d9eee05a1db3b9ce61a65f26c3ea6b3ac1235361c50b572ad6&bancode=d5e5cfd003f08ff443ed5d1512b7dd956cc42b62c589a1a1ad2cc735cc7af679#wechat_redirect

# 正常：直接跳转

# 非官方：https://weixin110.qq.com/cgi-bin/mmspamsupport-bin/newredirectconfirmcgi?click=27d99474a3d7440b2c3d2207f2bcec71&bankey=cb777468bc1265b84ed2fcf11c4bd5e5&midpagecode=67377a2adb44e17c1b0adb24b5cf2bd12c34d9b56e06ccd6dd4c291b423b5bd7ff6dabdc557c992f5d60d892b6870f745969d9037e32283635d15e8dad0f6d17763398d722719593518577149db03dd9&bancode=f8b31702e15a1b01ea780fc8c3fbd12404ed35538aba05916b9d207ca1d83047#wechat_redirect
