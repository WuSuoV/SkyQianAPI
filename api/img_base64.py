import base64

import requests
from urllib3 import disable_warnings

disable_warnings()


def img_to_base64_from_local(path):
    try:
        with open(path, 'rb') as f:
            image_base64 = base64.b64encode(f.read())
        return "data:image/png;base64," + str(image_base64)[2:-1]
    except Exception as e:
        return 'image is not exist'


def img_to_base64_from_url(url):
    try:
        r = requests.get(url, verify=False)
        if 'image' in r.headers.get('Content-Type') and int(r.headers.get('Content-Length')) <= (1024 * 1024):
            image_base64 = base64.b64encode(r.content)
            return "data:image/png;base64," + str(image_base64)[2:-1]
        else:
            return 'It is not a image or it is larger than 1MB'
    except:
        return 'Image is not exist'
