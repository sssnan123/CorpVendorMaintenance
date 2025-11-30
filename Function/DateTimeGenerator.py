from datetime import datetime, timedelta

def getPlannedTime(startTime, endTime, isWinter):

    if isWinter == "0":
        timeDiff = 7
    
    if isWinter == "1":
        timeDiff = 8

    # 打印做change的中国时间
    chinaTime = datetime.fromisoformat(startTime) + timedelta(hours=8) - timedelta(minutes=30)
    dayOfWeekInChina = chinaTime.strftime("%A")
    print("Day Of Week in China: " + dayOfWeekInChina)
    print("China Start Time CST: " + datetime.strftime(chinaTime, "%Y-%m-%d %H:%M:%S"))
    print("")

    # 写在implementation plan中美国时间
    plannedStartTime = datetime.fromisoformat(startTime) - timedelta(hours=timeDiff) - timedelta(minutes=30)
    print("America Start Time PT: " + str(plannedStartTime))
    plannedEndTime = datetime.fromisoformat(endTime) - timedelta(hours=timeDiff) + timedelta(minutes=30)
    print("America End Time PT: " + str(plannedEndTime))
    dayOfWeekInAmerica = plannedStartTime.strftime("%A")
    print("Day Of Week in America: " + dayOfWeekInAmerica)

    return plannedStartTime, plannedEndTime

def getStartTimeInPayloads(startTime):
    return datetime.strftime(datetime.fromisoformat(startTime) - timedelta(minutes=30), "%Y-%m-%d %H:%M:%S")

def getStartTimeInShortDescription(plannedStartTime):

    day = datetime.strftime(plannedStartTime, "%d")
    month = datetime.strftime(plannedStartTime, "%b")
    time = datetime.strftime(plannedStartTime, "%H%M")

    suffix = ""
    intDay = int(day)
    if (intDay < 11 or intDay > 13) and 0 < (intDay % 10) < 4:
        if(intDay % 10 == 1):
            suffix = "st"
        if(intDay % 10 == 2):
            suffix = "nd"
        if(intDay % 10 == 3):
            suffix = "rd"
    else:
        suffix = "th"

    startTimeInShortDescription = day + suffix + " " + month + " " + time + "PT"

    return startTimeInShortDescription

def getStartTimeInImplementation(plannedStartTime):
    startTimeInImplementation = datetime.strftime(plannedStartTime, "%H%M")
    return startTimeInImplementation

def getAllPartsOfDuration(plannedStartTime, plannedEndTime):

    # 需要维护的时间长度获取对应的日、时、分、秒
    allSeconds = (plannedEndTime - plannedStartTime).total_seconds()
    days = int(allSeconds / (3600 * 24))
    hours = int((allSeconds - (3600 * 24 * days)) / 3600)
    minutes = int((allSeconds - (3600 * 24 * days) - (3600 * hours)) / 60)
    seconds = int(allSeconds - (3600 * 24 * days) - (3600 * hours) - (60 * minutes))

    if days == 0:
        days = "00"
    else:
        days = str(days)

    if hours == 0:
        hours = "00"
    else:
        hours = str(hours)

    if minutes == 0:
        minutes = "00"
    else:
        minutes = str(minutes)

    if seconds == 0:
        seconds = "00"
    else:
        seconds = str(seconds)

    allMinutes = int(allSeconds / 60)

    changeDuration = days + " " + hours + ":" + minutes + ":" + seconds
    
    print("Change Duration: " + changeDuration)

    return days, hours, minutes, seconds, allMinutes

def getChangeDuration(plannedStartTime, plannedEndTime):
    days, hours, minutes, seconds, allMinutes = getAllPartsOfDuration(plannedStartTime, plannedEndTime)
    changeDuration = days + " " + hours + ":" + minutes + ":" + seconds
    return changeDuration

def getMinutesInShortDescription(plannedStartTime, plannedEndTime):
    days, hours, minutes, seconds, allMinutes = getAllPartsOfDuration(plannedStartTime, plannedEndTime)
    return str(allMinutes)

def getVendorTime(startTime, endTime, isWinter):

    if isWinter == "0":
        timeDiff = 7
    
    if isWinter == "1":
        timeDiff = 8

    vendorStartTime = datetime.fromisoformat(startTime) - timedelta(hours=timeDiff)
    print("Vendor Start Time PT: " + str(vendorStartTime))
    vendorEndTime = datetime.fromisoformat(endTime) - timedelta(hours=timeDiff)
    print("Vendor End Time PT: " + str(vendorEndTime))

    return vendorStartTime, vendorEndTime

def getVendorDuration(vendorStartTime, vendorEndTime):
    # 需要维护的时间长度获取对应的日、时、分、秒
    allSeconds = (vendorEndTime - vendorStartTime).total_seconds()
    durationDays = int(allSeconds / (3600 * 24))
    durationHours = int((allSeconds - (3600 * 24 * durationDays)) / 3600)
    durationMinutes = int((allSeconds - (3600 * 24 * durationDays) - (3600 * durationHours)) / 60)
    
    if durationMinutes == 30:
        vendorDuration = str(durationDays * 24 + durationHours) + ".5"
    else:
        vendorDuration = str(durationDays * 24 + durationHours)

    print("Vendor duration: " + vendorDuration)

    return vendorDuration

def getVendorTimeInImplementation(startTime, endTime, isWinter):

    vendorStartTime, vendorEndTime = getVendorTime(startTime, endTime, isWinter)
    vendorDuration = getVendorDuration(vendorStartTime, vendorEndTime)

    vendorStartTime = datetime.strftime(vendorStartTime, "%m/%d/%Y %H%MPT")
    vendorEndTime = datetime.strftime(vendorEndTime, "%m/%d/%Y %H%MPT")

    vendorTimeInImplementation = vendorStartTime + "  " + vendorEndTime + "  " + vendorDuration + " hours"

    return vendorTimeInImplementation

def isAmericaTimeOrNot(startTime, endTime, isWinter):

    plannedStartTime, plannedEndTime = getPlannedTime(startTime, endTime, isWinter)

    timeToStartWork = ""
    timeToEndWork = ""

    # 非冬令时的美国工作时间是07:00:00 - 18:59:59
    if isWinter == "0":
        timeToStartWork = datetime.fromisoformat(datetime.strftime(plannedStartTime, "%Y-%m-%d 07:00:00"))
        timeToEndWork = datetime.fromisoformat(datetime.strftime(plannedStartTime, "%Y-%m-%d 18:59:59"))
    
    # 冬令时的美国工作时间是06:00:00 - 17:59:59
    if isWinter == "1":
        timeToStartWork = datetime.fromisoformat(datetime.strftime(plannedStartTime, "%Y-%m-%d 06:00:00"))
        timeToEndWork = datetime.fromisoformat(datetime.strftime(plannedStartTime, "%Y-%m-%d 17:59:59"))

    if timeToStartWork <= plannedStartTime <= timeToEndWork:
        return True
    else:
        return False

