from urllib.parse import quote, unquote
import base64


def url_encode(url):
    return quote(url, safe='')


def url_decode(url):
    return unquote(url)


def base64_encode(text: str):
    bytes_data = base64.b64encode(text.encode('utf-8'))
    return bytes_data.decode('utf-8')


def base64_decode(text: str):
    return base64.b64decode(text).decode('utf-8')
