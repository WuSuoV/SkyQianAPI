import os
import re
import time
import requests
from config import myconfig

class qqnum:
    id: dict = {'name': None,
                'imgpath': myconfig.get('rootpath') + '/static/image'}

    def __init__(self, qq):
        self.id['name'] = qq

    def Get_bkn(self, pSkey):
        # 计算bkn
        t, n, o = 5381, 0, len(pSkey)
        while n < o:
            t += (t << 5) + ord(pSkey[n])
            n += 1
        return t & 2147483647

    def Get_ptqrToken(self, qrsig):
        # 计算ptqrtoken
        n, i, e = len(qrsig), 0, 0
        while n > i:
            e += (e << 5) + ord(qrsig[i])
            i += 1
        return 2147483647 & e

    def Get_QRcode(self):
        # 获取 腾讯网 二维码
        url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&t=0.8692955245720428&daid=5&pt_3rd_aid=0'

        try:
            r = requests.get(url)
            qrsig = requests.utils.dict_from_cookiejar(r.cookies).get('qrsig')

            with open(self.id['imgpath'] + '/' + self.id['name'] + '.png', 'wb') as f:
                f.write(r.content)

            print(time.strftime('%H:%M:%S'), ' 登录二维码获取成功')
            return qrsig
        except Exception as e:
            print(time.strftime('%H:%M:%S') + " 获取二维码报错" + str(e))
            print('第' + str(e.__traceback__.tb_lineno) + '行文件报错')

    def Get_QQ(self):

        global qq_number
        # 获取cookie
        qrsig = self.Get_QRcode()
        ptqrtoken = self.Get_ptqrToken(qrsig)
        start_time = time.time()
        while time.time() - start_time <= 30:
            url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptqrtoken=' + str(
                ptqrtoken) + '&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-' + str(
                time.time()) + '&js_ver=20032614&js_type=1&login_sig=&pt_uistyle=40&aid=549000912&daid=5&'
            cookies = {'qrsig': qrsig}

            try:
                r = requests.get(url, cookies=cookies)
                if '二维码未失效' in r.text:
                    # print(time.strftime('%H:%M:%S'), ' 二维码未失效')
                    pass
                elif '二维码认证中' in r.text:
                    print(time.strftime('%H:%M:%S'), ' 二维码认证中')
                elif '二维码已失效' in r.text:
                    print(time.strftime('%H:%M:%S'), ' 二维码已失效')
                    qrsig = self.Get_QRcode()
                    ptqrtoken = self.Get_ptqrToken(qrsig)
                else:
                    print(time.strftime('%H:%M:%S'), ' 登录成功!!!')

                    qq_number = re.findall(r'&uin=(.+?)&service', r.text)[0]
                    return qq_number
            except Exception as e:
                print(time.strftime('%H:%M:%S') + " 获取cookie报错" + str(e))
                print('第' + str(e.__traceback__.tb_lineno) + '行文件报错')
            time.sleep(2)
        print(time.strftime('%H:%M:%S'), ' 已超时')
        return 'timeout'

