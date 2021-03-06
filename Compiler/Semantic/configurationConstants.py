import sys
sys.path.append("..")

from Utils import createCube
from Compiler.DataStructures.symbolTable import Symbol

def processConfigConstants(configBranch, symbolTable):
    lookupList = ['timer', 'timeUnit', 'rows', 'columns', 'cube']
    for son in configBranch.getSons():
        for keyword in lookupList:
            name = son.getName()
            if name == "cube":
                cubeValue = son.getSon(2)
                if cubeValue.getName() == "list":
                    from semanticAnalysis import listElements
                    tempValue = listElements(cubeValue.getSon(1), [])
                else:
                    tempValue = createCube(3, 8, False)
                tempSymbol = Symbol(son.getSon(0).getName(), tempValue, "Reserved", "global")
                symbolTable.addReservedId(son.getSon(0).getName())
                symbolTable.add(tempSymbol)
                break
            elif name == keyword:
                tempValue = son.getSons()[2].getName()
                tempSymbol = Symbol(son.getName(), tempValue, "Reserved", "global")
                symbolTable.addReservedId(son.getSon(0).getName())
                symbolTable.add(tempSymbol)
                break
            elif keyword == lookupList[-1]:
                return False
    return True
