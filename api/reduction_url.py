import requests


def reduction(url):
    try:
        res = requests.get(url, allow_redirects=False).headers.get('Location')
    except:
        return {
            'code': 400,
            'statu': 'error',
            'msg': 'URL not accessible'
        }

    if res is None:
        return {
            'code': 400,
            'statu': 'error',
            'msg': 'it is not a short url'
        }
    else:
        return {
            'code': 200,
            'statu': 'success',
            'url': res
        }
