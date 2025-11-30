import json
import os
import requests
from . import PayloadsGenerator

# 打开proxies文件，导入代理
with open(os.getcwd().rsplit("/", 0)[0] + "/proxies.json") as json_profile:
    proxies = json.load(json_profile)

# 创建ticket
def createChange(startTime, endTime, isWinter, assignee, validCircuitsList):

    payloads = PayloadsGenerator.getPayloads(startTime, endTime, isWinter, assignee, validCircuitsList)

    createChangeUrl = "https://ebaysnow.vip.ebay.com/api/message/send"

    createChangeHeaders = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "Authorization" : "Basic dV9zYV9lYmF5X3Nub3dfbmV0OlJlc3RpbnBlYWNldHJhY2UyMDIw"
    }

    response = requests.post(createChangeUrl, headers = createChangeHeaders, json = payloads, verify = "/usr/share/ca-certificates/eBayROOT/eBay_ROOT_CA.crt")

    uiLink = json.loads(response.text)["ui_link"]

    print("SNOW URL: " + uiLink)
