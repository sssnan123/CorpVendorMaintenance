import requests
import sys
sys.path.append("..")
from Class import LoginInfo
import os
import json

# 打开settings文件，导入参数
with open(os.getcwd().rsplit("/", 0)[0] + "/settings.json") as json_profile:
    data = json.load(json_profile)

# 打开proxies文件，导入代理
with open(os.getcwd().rsplit("/", 0)[0] + "/proxies.json") as json_profile:
    proxies = json.load(json_profile)

# 获取token的URI
get_token_uri = 'https://login.salesforce.com/services/oauth2/token'

# 发送post请求获取参数，返回LoginInfo对象
def getLoginInfo() :
    response = requests.post(get_token_uri,
                                proxies = proxies,
                                data = data
                            )

    # 将response中的json转换成对象
    responseLoginInfo = json.loads(response.text)
    return LoginInfo.LoginInfo(
                responseLoginInfo["access_token"],
                responseLoginInfo["instance_url"],
                responseLoginInfo["token_type"]
            )
