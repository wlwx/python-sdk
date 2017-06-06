#!/usr/bin/python3
# -*- coding:utf-8 -*-
#filename:Demo
__author__ = 'zhouzhao'
import requests,json,hashlib
from urllib.parse import quote

def send_sms():
    # 短信提交地址，请联系管理员获取
    url = 'http://127.0.0.1:8861'
    # 用户账号，必填
    uid = "XXXXXX"
    # 用户密码，必填
    pwd = "XXXXXXXXX"
    # 长号码，选填
    srcphone = "10690013365412"
    package1 = {'phone':'15960393654','context':'您的验证码为：8888'}
    package2 = {'phone':'18650995293','context':'您的验证码为：9999'}
    list = [package1,package2]
    msg = json.dumps(list, ensure_ascii=False).replace(' ','')
    sign = quote(msg) + pwd
    sign = sign.encode('utf-8')
    m = hashlib.md5()
    m.update(sign)
    sign = m.hexdigest()
    data = {}
    data['uid'] = uid
    data['srcphone'] = srcphone
    data['msg'] = msg
    data['sign'] = sign
    _headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    r = requests.post(url, data=data, headers=_headers, timeout=5)
    r.encoding = 'utf-8'
    print(r.content)

if __name__ == '__main__':
    # 批量发送短信
    send_sms()