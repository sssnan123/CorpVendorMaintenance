import re
from . import ChooseUser
import sys
sys.path.append("..")
from Function import RequestGenerator

# 选择时间菜单
def pickTimeMenu(validCircuitsList):
    isConfirmed = False
    while isConfirmed == False:
        # 是否需要开ticket
        needToOpenTicket = input("Need to open change ticket? (Please input 0 or 1) ")
        pattern = "[0,1]"
        if re.match(pattern, needToOpenTicket) is not None:
            # 输入0退出时间选择菜单
            if needToOpenTicket == "0":
                print("No need to open ticket")
                isConfirmed = True
            # 输入1选择时间开ticket
            if needToOpenTicket == "1":
                print("Open ticket")
                startTime = ""
                isConfirmedStartTime = False
                while isConfirmedStartTime == False:
                    # 输入合法的开始时间
                    startTime = input("Please enter the start time: (UTC/GMT yyyy-mm-dd hh:mm) ")
                    pattern = "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$"
                    if re.match(pattern, startTime) is not None:
                        isConfirmedStartTime = True
                        print(startTime)
                    else:
                        print("Please input legal value")
                        isConfirmedStartTime = False
                endTime = ""
                isConfirmedEndTime = False
                while isConfirmedEndTime == False:
                    # 输入合法的结束时间
                    endTime = input("Please enter the end time: (UTC/GMT yyyy-mm-dd hh:mm) ")
                    pattern = "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$"
                    if re.match(pattern, endTime) is not None:
                        isConfirmedEndTime = True
                        print(endTime)
                    else:
                        print("Please input legal value")
                        isConfirmedEndTime = False
                isWinter = ""
                isConfirmedWinter = False
                while isConfirmedWinter == False:
                    # 输入是否为冬令时
                    isWinter = input("Is Winter? (0: False, 1: True) ")
                    pattern = "[0,1]"
                    if re.match(pattern, isWinter) is not None:
                        if isWinter == "0":
                            isConfirmedWinter = True
                            print("False")
                        if isWinter == "1":
                            isConfirmedWinter = True
                            print("True")
                    else:
                        print("Please input legal value")
                        isConfirmedWinter = False
                assignee = ChooseUser.generatePickUsersMenu(startTime, endTime, isWinter)
                RequestGenerator.createChange(startTime, endTime, isWinter, assignee, validCircuitsList)
                isConfirmed = True
        else:
            print("Please input legal value")
            isConfirmed = False
