from Menu import ChooseOneOrMoreCircuits
import re

# 主菜单
def MainMenu():
    menuDescription = (
        "\nMenu Info：（Please Input Number）：\n"
        "  1. Open Change Ticket\n"
        "  0. Exit\n"
        "Which function: "
    )

    strict = "[0,1]"

    confirmed = False
    while confirmed != True:
        inputValue = input(menuDescription)
        if re.match(strict, inputValue) is not None:
            if inputValue == "0":
                confirmed = True
            if inputValue == "1":
                ChooseOneOrMoreCircuits.chooseOneOrMoreCircuitsMenu()
        else:
            print("Input number is illegal, Please re-enter! ")

if __name__ =="__main__":
    MainMenu()