from . import getLoginInfo
import sys
sys.path.append("..")
from Class import CircuitInfo
import os
import json

# 打开proxies文件，导入代理
with open(os.getcwd().rsplit("/", 0)[0] + "/proxies.json") as json_profile:
    proxies = json.load(json_profile)

# 通过LoginInfo获取access_token、instance_url、token_type参数
login_info = getLoginInfo.getLoginInfo()
access_token = login_info.getAccessToken()
instance_url = login_info.getInstanceUrl()
token_type = login_info.getTokenType()

# 构造queryURL和searchURL
baseURI = "/services/data/v52.0"
queryAPI = baseURI + "/query"
searchAPI = baseURI + "/search"
queryUrl = instance_url + queryAPI
searchUrl = instance_url + searchAPI

# Token用来授权访问SalesForce API
headers = {
    "Authorization" : token_type + " " + access_token
}

# 通过search api搜索Cicuit Id信息
def getCircuitsList(circuit_id):
    # search api的SOSL查询语言
    paramsForId = {
        "q" : "FIND{" + circuit_id + "}"
    }

    # 获取Cicuit Id信息中所有的Asset Id
    response = getLoginInfo.requests.get(
                        searchUrl,
                        params = paramsForId,
                        proxies = proxies,
                        headers = headers)
    # 将response的json信息转换成json对象并获取searchRecords信息
    searchRecords = getLoginInfo.json.loads(response.text)["searchRecords"]

    CircuitsList = []
    # 遍历Circuit Id中所有的Asset Id
    for circuitInfo in searchRecords:
        if(circuitInfo["attributes"]["type"] == "Asset__c"):
            # 根据Asset Id获取Asset信息
            circuits = getAsset(circuitInfo["Id"])
            # 查询到的链路信息添加到List中
            CircuitsList.append(circuits)

    return CircuitsList

# 通过query api查询Asset Id对应的所有链路信息
def getAsset(asset_id):
    # query api的SOQL查询语言
    assetFields = (
                    'Vendor_ID__c, '
                    'Vendor__r.Name, '
                    'A_End_Port_Assignment__c, '
                    'Z_End_Port_Assignment__c, '
                    'Status__c, '
                    'Corp_Site__c '
    )

    paramsForQuery = {
        "q" : "SELECT " + assetFields + "FROM Asset__c WHERE Id = '" + asset_id + "'"
    }

    # 获取Circuit Id对应的资产信息
    response = getLoginInfo.requests.get(
                            queryUrl,
                            params = paramsForQuery,
                            proxies = proxies,
                            headers = headers)
    # 将response的json转换成json对象并获取records信息
    records = getLoginInfo.json.loads(response.text)["records"][0]

    return CircuitInfo.CircuitInfo(
            records["Vendor_ID__c"],
            records["A_End_Port_Assignment__c"],
            records["Z_End_Port_Assignment__c"],
            records["Vendor__r"]["Name"],
            records["Status__c"],
            records["Corp_Site__c"]
    )
