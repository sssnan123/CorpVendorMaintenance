import re
import sys
sys.path.append("..")
from Function import DateTimeGenerator

shiftOnAmerica = [
    "tcraig", 
    "syeshah", 
    "ayreddy", 
    "nvejendla", 
    "ssiddamshetty", 
    "vkarnam",
    "sisreeram",
    "sshrinivasprabhu",
    "agrandhi"
]

shiftOnChina = [
    "junsma",
    "renrzhang",
    "xiangdhe",
    "menghazhu"
]

# 生成选择用户菜单
def generatePickUsersMenu(startTime, endTime, isWinter):

    availableUsers = []

    if DateTimeGenerator.isAmericaTimeOrNot(startTime, endTime, isWinter):
        availableUsers = shiftOnAmerica
    else:
        availableUsers = shiftOnChina

    # 生成菜单选项描述
    optionList = ""
    strictPattern = ""
    for index, option in enumerate(availableUsers):
        optionList = optionList + str(index) + ". " + option + "\n"
        if index != (len(availableUsers) - 1):
            strictPattern = strictPattern + str(index) + ","
        else:
            strictPattern = strictPattern + str(index)
    
    menuDescription = "Available users:\n" + optionList + "\n"

    strict = "[" + strictPattern + "]"

    while True:
        pickUser = input(menuDescription + "Choose which user: ")
        if re.match(strict, pickUser) is not None:
            print(availableUsers[int(pickUser)] + "\n")
            return availableUsers[int(pickUser)]
        else:
            print("Input number is illegal, Please re-enter!")
