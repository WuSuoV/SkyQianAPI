# SkyQian's API

欢迎来到SkyQian的API，大部分功能都是自行实现，而非盗用所谓的第三方接口，套娃行为可没什么意思。

## API列表

记得加上参数 `?token=xxxxx`

1. [/api/wxred/](/api/wxred/) : 检测域名是否被微信拦截。
2. [/api/dwz/](/api/dwz/) : 生成短网址，调用 dwz.wa 的api
3. [/api/jwz/](/api/jwz/) : 还原短网址。
4. `/api/qqnum/` : 参数qq（必选），值为你待验证的QQ号。扫码验证与目标QQ是否相符，点开有步骤说明。
5. [/api/imgbase64/](/api/imgbase64/) : 图片转base64格式。
6. [/api/qqmusic/](/api/qqmusic/) : 增加QQ音乐时长
7. [/api/onedrive/](/api/onedrive/) : 获取OneDrive文件分享的直链，仅限于单文件、非个人版。
8. [/api/search/](/api/search/) : 通过关键字搜索1OVE论坛中的资源
9. [/api/yiyan/](/api/yiyan/) : 返回一个有意思的句子（一言）
10. [/api/randompasswd/](/api/randompasswd/) : 生成随机密码，可选参数num: int，不加默认为16
11. [/api/email/](/api/email/) : 参数text：需要发送的文本（必选），邮箱的配置进入配置文件设置
12. [/api/urlcode/](/api/urlcode/) : mode为encode或者decode，代表编码和解码。url为所要编码的网址
13. [/api/base64/](/api/base64/) : mode为encode或者decode，text：如果是编码就输入文字，如果是解码就只能输入base64格式的编码
14. [/api/translate/](/api/translate/) : 有道翻译接口，参数为text：需要翻译的文本，自动检测文本语言类型

可以自行搭建，项目已开源。 

## 项目地址

Github：[https://github.com/Qiantigers/SkyQianAPI](https://github.com/Qiantigers/SkyQianAPI)

## 使用说明

Python版本：3.8以上

使用框架：Flask

运行建议使用gunicorn，下载源码后，只需要更改 `config.py` 中的相关配置。

## 结语

经验不多，代码写的不是很优雅。

我的博客：[www.skyqian.com](https://www.skyqian.com/?from=github.com/Qiantigers/SkyQianAPI)
