import requests


def reduction(url):
    try:
        res = requests.get(url, allow_redirects=False).headers.get('Location')
    except:
        return {'statu': 'error', 'msg': 'URL not accessible'}

    if res is None:
        return {'statu': 'error', 'msg': 'it is not a short url'}
    else:
        return {'statu': 'success', 'url': res}


if __name__ == '__main__':
    url = 'http://hooqian.comm'
    print(reduction(url))