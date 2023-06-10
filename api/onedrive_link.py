import re

def judgeLink(url):
    reg1 = r'https://.+sharepoint\.com'
    reg2 = r'personal/(\w+?)/'
    reg3 = r'.*/(\S+)'
    reg4 = r'com/:(\w):/'

    p1 = re.findall(reg1, url)[0]
    p2 = re.findall(reg2, url)[0]
    p3 = re.findall(reg3, url)[0]

    if '?' in p3:
        p3 = re.findall(r'(\S+?)\?', p3)[0]

    if re.findall(reg4, url)[0] == 'f':
        return {'link': 'invalid', 'msg': "抱歉，你所输入链接分享的是文件夹，直链生成仅对单文件有效。"}

    return {'link': p1 + '/personal/' + p2 + '/_layouts/52/download.aspx?share=' + p3, 'statu': 'success'}
