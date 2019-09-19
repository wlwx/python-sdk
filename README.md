# python-sdk
The http://wlwx.com python sdk.

在使用SDK之前，您需要有一对有效的cust_code和cust_pwd。如果不记得，可咨询我们的客服人员。


场景化示例

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
#filename:SdkTest
from wlwx.SmsOperator import SmsOperator
from wlwx.MultiSmsOperator import MultiSmsOperator
import json

__author__ = 'zhouzhao'

cust_code='XXXXXX'
cust_pwd='XXXXXXXXXX'
smsOperator = SmsOperator(cust_code,cust_pwd)

#发送普通短信（业务标识uid选填）
result = smsOperator.send_comSms({'destMobiles': '159XXXX3654', 'content': '您的验证码是6670','uid':'1234'})
print(result.content)

#发送变量短信
var1 = {'mobile':'159XXXX3654','vars':['长乐','25']}
var2 = {'mobile':'186XXXX5293','vars':['上杭','27']}
result = smsOperator.send_varSms({'content': '${mobile}用户您好，今天${var1}的天气，晴，温度${var2}度，事宜外出。', 'params': [var1,var2]})
print(result.content)

#获取状态报告
result = smsOperator.get_report()
print(result.content)

#获取用户上行
result = smsOperator.get_mo()
print(result.content)

#获取账户余额
result = smsOperator.get_account()
print(result.content)

#批量发送短信（长号码srcphone选填）
multiSmsOperator = MultiSmsOperator(cust_code,cust_pwd)
srcphone = "10690013365412"
package1 = {'phone': '159XXXX3654', 'context': '您的验证码为：8889'}
package2 = {'phone': '186XXXX5293', 'context': '您的验证码为：9990'}
item = [package1,package2]
result = multiSmsOperator.send_multiSms({'item':item,'srcphone':srcphone})
print(result.content)
```

