from . import EnterCircuit
import re

# 选择一个还是多个链路的菜单
def chooseOneOrMoreCircuitsMenu():
    print("\nChooseOneOrMoreCircuitsMenu")
    isMultiplyCircuits = input("Is multiple circuits? (Please input 0 or 1) ")
    pattern = "[0,1]"
    if re.match(pattern, isMultiplyCircuits) is not None:
        if isMultiplyCircuits == "0":
            EnterCircuit.singleCircuitMenu()
        if isMultiplyCircuits == "1":
            EnterCircuit.multipleCircuitsMenu()
    else:
        print("Please input legal info")