# 获取CIS
def getCIS(validCircuitsList):

    cis = []

    for item in validCircuitsList:
        if item != validCircuitsList[-1]:
            component = item.getVendorName() + ":" + item.getVendorId() + "\n" + item.getAEndPort() +  "\n" + item.getZEndPort() + "\n"
            cis.append(component)
        else:
            component = item.getVendorName() + ":" + item.getVendorId() + "\n" + item.getAEndPort() +  "\n" + item.getZEndPort()
            cis.append(component)

    return cis

# 获取Declaration中的CIS信息
def getCISInDeclaration(cis):
    cisInDeclarartion = ""
    for component in cis:
        # 如果不是最后一个有效组件时
        if component != cis[-1]:
            cisInDeclarartion = cisInDeclarartion + component + "\n"
        else:
            cisInDeclarartion = cisInDeclarartion + component
    return cisInDeclarartion
