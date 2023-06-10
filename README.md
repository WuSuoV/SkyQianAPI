# SkyQian's API

欢迎来到SkyQian的API，大部分功能都是自行实现，而非盗用所谓的第三方接口，套娃行为可没什么意思。

## API列表

记得加上参数 `?token=xxxxx`

1. `/api/wxred/{url}` : 检测域名是否被微信拦截。
2. `/api/dwz/{url}` : 生成短网址，调用 dwz.wa 的api
3. `/api/jwz/{url}` : 还原短网址。
4. `/api/qqnum` : 扫码验证与目标QQ是否相符，点开有步骤说明。
5. `/api/imgbase64/{url}` : 图片转base64格式。
6. `/api/qqmusic/listen-time/{qq}` : 增加QQ音乐时长
7. `/api/onedrive/zl/{url}` : 获取OneDrive文件分享的直链，仅限于单文件、非个人版。
8. `/api/search/bbs/{keywords}` : 通过关键字搜索1OVE论坛中的资源
9. `/api/yiyan` : 返回一个有意思的句子（一言）
10. `/api/randompasswd` : 生成随机密码，可选参数num: int，不加默认为16

可以自行搭建，项目已开源。 

## 项目地址

Github：[https://github.com/Qiantigers/SkyQianAPI](https://github.com/Qiantigers/SkyQianAPI)

## 使用说明

Python版本：3.8

使用框架：Flask

运行建议使用gunicorn，下载源码后，只需要更改 `config.py` 中的相关配置。

## 结语

经验不多，代码写的不是很优雅。