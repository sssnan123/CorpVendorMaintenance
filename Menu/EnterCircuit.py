import re
from . import PickTime
import sys
sys.path.append("..")
from GetInfo import getCircuitsList

# 添加所有有效的链路到列表
def addValidCircuitsToList(validCircuitsList):

    # 输入Circuit Id
    circuit_id = input("Please input Circuit Id: ")

    # 去除多余空格
    circuit_id = re.sub(r"\s+", "", circuit_id)

    # 若没有输入值则直接退出
    if circuit_id == "":
        return

    # 替换输入值中的-
    if "-" in circuit_id:
        circuit_id = circuit_id.replace("-", "?")

    CircuitsList = getCircuitsList.getCircuitsList(circuit_id)

    # 遍历所有链路判断段是否可用
    for item in CircuitsList:
        # 打印链路信息
        print(item.getVendorId() + " ---- " + item.getVendorName() + " ---- " + item.getAEndPort() + " ---- " + item.getZEndPort() + " ---- " + item.getStatus() + " ---- " + item.getCorpSite())
        # 若状态是Provisioned且属于Corp就是有效的链路
        if (item.getStatus() == "Provisioned" and item.getCorpSite() == "Corp" and item.getZEndPort() != ""):
            validCircuitsList.append(item)
    print("\n")

    # 打印所有有效链路信息
    for item in validCircuitsList:
        print("Valid record  is： " + item.getVendorId() + " ---- " + item.getVendorName() + " ---- " + item.getAEndPort() + " ---- " + item.getZEndPort() + " ---- " + item.getStatus() + " ---- " + item.getCorpSite())


# 打开单个链路的菜单
def singleCircuitMenu():
    validCircuitsList = []
    print("\nSingle Circuit Menu")
    addValidCircuitsToList(validCircuitsList)
    if len(validCircuitsList) == 0:
        return
    PickTime.pickTimeMenu(validCircuitsList)

# 打开多个链路的菜单
def multipleCircuitsMenu():
    validCircuitsList = []
    print("Multiple Circuits Menu")
    stillNeedInput = True
    # 循环输入Circuit Id
    while stillNeedInput == True:
        addValidCircuitsToList(validCircuitsList)
        # 判定是否需要继续输入链路信息
        isConfirmed = False
        while isConfirmed == False:
            wantToExit = input("Do you want to continue adding circuits?: (Please input 0 or 1) ")
            pattern = '[0, 1]'
            if re.match(pattern, wantToExit) is not None:
                if wantToExit == "0":
                    isConfirmed = True
                    stillNeedInput = False
                if wantToExit == "1":
                    isConfirmed = True
                    stillNeedInput = True
            else:
                print("Please input 0 or 1")
                isConfirmed = False
    
    if len(validCircuitsList) == 0:
        return
    PickTime.pickTimeMenu(validCircuitsList)

