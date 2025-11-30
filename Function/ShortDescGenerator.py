from . import DateTimeGenerator

# 获取Short Description
def getShortDescription(plannedStartTime, plannedEndTime, validCircuitsList):

    shortDescription = "CORP VENDOR DOWN " 

    # 获取Short Description中的起始时间
    startTimeInShortDescription = DateTimeGenerator.getStartTimeInShortDescription(plannedStartTime)

    # 获取Short Description中的Minutes
    minutesInShortDescription = DateTimeGenerator.getMinutesInShortDescription(plannedStartTime, plannedEndTime)

    # 如果是多个组件
    if len(validCircuitsList) >= 2:
        shortDescription = shortDescription + validCircuitsList[0].getVendorName() + " : " + "See The Components @ " + startTimeInShortDescription + ", " + minutesInShortDescription + " MINUTES"
    else:
        shortDescription = shortDescription + validCircuitsList[0].getVendorName() + " : " + validCircuitsList[0].getAEndPort() + " <> " + validCircuitsList[0].getZEndPort() + " @ " + startTimeInShortDescription + ", " + minutesInShortDescription + " MINUTES(" + validCircuitsList[0].getVendorName() + ":" + validCircuitsList[0].getVendorId() + ")"

    return shortDescription

