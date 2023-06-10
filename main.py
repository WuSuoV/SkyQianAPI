import re
from flask import Flask, request, jsonify
from api import *
from security import token
from config import myconfig
from tools import introduction
from tools.jsonxasc import jsonxasc

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
safe = token.Token(myconfig.get('token'))


@app.route('/')
# @safe.verify_token
def index():
    return introduction.introduction()


@app.route('/api/search/bbs/<keywords>', methods=['GET'])
@safe.verify_token
def search_bbs(keywords):
    return jsonxasc(search.search_from_1ovebbs(keywords))


@app.route('/api/qqmusic/listen-time/<int:qq>', methods=['GET'])
@safe.verify_token
def listen(qq):
    return jsonxasc(qqmusic.listen_time(qq))

@app.route('/api/yiyan', methods=['GET'])
@safe.verify_token
def yi_yan():
    return jsonxasc(yiyan.yiyan())


@app.route('/api/wxred/<path:url>', methods=['GET'])
@safe.verify_token
def wxred(url):
    res = detect_domain_in_tencent.get_res(url)
    return res


@app.route('/api/onedrive/zl/<path:url>', methods=['GET'])
@safe.verify_token
def zl(url):
    return onedrive_link.judgeLink(url)


@app.route('/api/dwz/<path:url>', methods=['GET'])
@safe.verify_token
def dwz(url):
    return short_url.short(url)


@app.route('/api/jwz/<path:url>', methods=['GET'])
@safe.verify_token
def jwz(url):
    return reduction_url.reduction(url)


@app.route('/api/qqnum', methods=['GET'])
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


@app.route('/api/qqnum/img', methods=['GET'])
@safe.verify_token
def qqnum_img():
    qq = request.args.get('qq')
    base64 = img_base64.img_to_base64_from_local(f"{myconfig.get('rootpath')}/static/image/{qq}.png")
    return f'<div style="text-align: center;"><img src="{base64}"></div>'


@app.route('/api/qqnum/<qq>', methods=['GET'])
@safe.verify_token
def qqnum_qq(qq):
    myqq = qqnumber.qqnum(qq)
    your_qq = myqq.Get_QQ()
    if qq == your_qq:
        # os.remove(myqq.id['imgpath'] + '/' + myqq.id['name'] + '.png')
        return {'statu': 'success', 'sample qq': qq, 'your qq': your_qq,
                'msg': 'Your QQ is the same as the detected QQ'}
    else:
        return {'statu': 'failure', 'sample qq': qq, 'your qq': your_qq,
                'msg': 'Your QQ is different from the detected QQ, please check the QQ you used to scan the code'}


@app.route('/api/imgbase64/<path:url>', methods=['GET'])
@safe.verify_token
def imgbase64(url):
    flag = re.match(r'http[s]://', url)
    if flag is not None:
        return {'base64': img_base64.img_to_base64_from_url(url)}


@app.route('/api/randompasswd', methods=['GET'])
@safe.verify_token
def randompasswd():
    num = request.args.get('num')
    if num is None:
        return {'password': random_password.passwd(16), 'length': 16}
    else:
        return {'password': random_password.passwd(int(num)), 'length': int(num)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12138)
else:
    application = app
