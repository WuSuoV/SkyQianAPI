import re
from flask import Flask, request, render_template, url_for
from api import *
from config import myconfig
from security import token
from tools import introduction
from tools.param import param_value
from tools.jsonxasc import jsonxasc

app = Flask(__name__)
safe = token.Token(myconfig.get('token'))


@app.route('/')
# @safe.verify_token
def index():
    return render_template('index.html', introduction=introduction.introduction())


@app.route('/api/urlcode/<mode>/<path:url>/', methods=['GET', 'POST'])
@safe.verify_token
def url_code(mode, url):
    print(url)
    if mode == 'encode':
        return jsonxasc({
            'code': 200,
            'msg': '编码',
            'data': codec.url_encode(url)
        })
    if mode == 'decode':
        return jsonxasc({
            'code': 200,
            'mode': '解码',
            'result': codec.url_decode(url)
        })

    return {
        'code': 500,
        'msg': 'error'
    }


@app.route('/api/translate/youdao/', methods=['GET', 'POST'])
@safe.verify_token
def trans_youdao():
    text = param_value('text')
    return jsonxasc(translate.youdao(text))


@app.route('/api/base64/<mode>/<text>/', methods=['GET', 'POST'])
@safe.verify_token
def base64(mode, text):
    if mode == 'encode':
        return jsonxasc({
            'mode': '编码',
            'text': text,
            'base64': codec.base64_encode(text)
        })
    if mode == 'decode':
        try:
            return jsonxasc({
                'code': 200,
                'msg': '解码',
                'base64': text,
                'data': codec.base64_decode(text)
            })
        except Exception:
            return jsonxasc({
                'code': 400,
                'mode': '解码',
                'base64': text,
                'msg': '检查一下你输入的格式正确吗？'
            })

    return {
        'code': 500,
        'msg': 'error'
    }


@app.route('/api/email/', methods=['GET', 'POST'])
@safe.verify_token
def email():
    text = param_value('text')
    e = aemail.aemail()
    e.set_text(text)
    msg = e.send()
    if msg == 'success':
        return jsonxasc({
            'code': 200,
            'msg': msg,
            'data': text
        })
    else:
        return jsonxasc({
            'code': 500,
            'msg': '邮件发送失败，请检查你的邮件配置。'
        })


@app.route('/api/search/bbs/<keywords>/', methods=['GET'])
@safe.verify_token
def search_bbs(keywords):
    return jsonxasc(search.search_from_1ovebbs(keywords))


@app.route('/api/qqmusic/listen-time/<int:qq>/', methods=['GET'])
@safe.verify_token
def listen(qq):
    return jsonxasc(qqmusic.listen_time(qq))


@app.route('/api/yiyan/', methods=['GET'])
@safe.verify_token
def yi_yan():
    return jsonxasc(yiyan.yiyan())


@app.route('/api/wxred/<path:url>/', methods=['GET'])
@safe.verify_token
def wxred(url):
    res = detect_domain_in_tencent.get_res(url)
    return jsonxasc(res)


@app.route('/api/onedrive/zl/<path:url>/', methods=['GET'])
@safe.verify_token
def zl(url):
    return jsonxasc(onedrive_link.judgeLink(url))


@app.route('/api/dwz/<path:url>/', methods=['GET'])
@safe.verify_token
def dwz(url):
    return jsonxasc(short_url.short(url))


@app.route('/api/jwz/<path:url>/', methods=['GET'])
@safe.verify_token
def jwz(url):
    return jsonxasc(reduction_url.reduction(url))


@app.route('/api/qqnum/', methods=['GET'])
@safe.verify_token
def qqnum():
    qq = request.args.get('qq')
    return '验证步骤：<br />' \
           '1. 点击开始验证<br />' \
           '2. 点击获取图片<br />' \
           '3. 打开qq，进行扫码，成功后页面会返回数据<br />' \
           '注意：验证时间会30s，请勿超时！<br />' \
           f'<a href="/api/qqnum/{qq}?&token={request.args.get("token")}">开始验证</a>&emsp;&emsp;' \
           f'<a href="/api/qqnum/img?qq={qq}&token={request.args.get("token")}" target="_blank">获取图片</a>'


@app.route('/api/qqnum/img/', methods=['GET'])
@safe.verify_token
def qqnum_img():
    qq = request.args.get('qq')
    base64 = img_base64.img_to_base64_from_local(f"{myconfig.get('rootpath')}/static/image/{qq}.png")
    return f'<div style="text-align: center;"><img src="{base64}"></div>'


@app.route('/api/qqnum/<qq>/', methods=['GET'])
@safe.verify_token
def qqnum_qq(qq):
    myqq = qqnumber.qqnum(qq)
    your_qq = myqq.Get_QQ()
    if qq == your_qq:
        return jsonxasc({
            'code': 200,
            'status': 'success',
            'sample qq': qq,
            'your qq': your_qq,
            'msg': 'Your QQ is the same as the detected QQ'
        })
    else:
        return jsonxasc({
            'code': 500,
            'status': 'failure',
            'sample qq': qq, 'your qq': your_qq,
            'msg': 'Your QQ is different from the detected QQ, please check the QQ you used to scan the code'
        })


@app.route('/api/imgbase64/<path:url>/', methods=['GET'])
@safe.verify_token
def imgbase64(url):
    flag = re.match(r'http[s]://', url)
    if flag is not None:
        return jsonxasc({
            'code': 200,
            'base64': img_base64.img_to_base64_from_url(url)
        })
    else:
        return jsonxasc({
            'code': 500,
            'msg': 'error'
        })


@app.route('/api/randompasswd/', methods=['GET'])
@safe.verify_token
def randompasswd():
    num = request.args.get('num')
    if num is None:
        return jsonxasc({
            'code': 200,
            'password': random_password.passwd(16),
            'length': 16
        })
    else:
        return jsonxasc({
            'code': 200,
            'password': random_password.passwd(int(num)),
            'length': int(num)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12138, debug=True)
else:
    application = app
