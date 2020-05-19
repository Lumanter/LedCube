import sys
sys.path.append("..")
from Utils import isAList, getIndexes
from CodeProduction.codeGenerator import *


# List T, F, Neg Operations
def listOperation(node, symbolTable, scope):
    # needs fix because of circular imports issue
    isReadyForRun = True
    if isReadyForRun:
        id = node.getSon(0).getSon(0).getName()

        if symbolTable.hasSymbol(id):

            oldList = symbolTable.getSymbol(id).getByIndex(0).getValue().getValue()

            if isAList(oldList):
                import copy
                newList = copy.deepcopy(oldList)

                listOperationWithIndex = (node.getSon(0).getSon(2).getName() == '.')
                if (listOperationWithIndex):
                    indexes = getIndexes(node.getSon(0).getSon(1), [], symbolTable, scope)
                    listOperator = node.getSon(0).getSon(3).getName()
                    replaceAtIndexWithOperator(newList, indexes, listOperator)
                else :
                    listOperator = node.getSon(0).getSon(2).getName()
                    replaceWithOperator(newList, listOperator)

                if (id == "Cubo"):
                    reportCubeChanges(oldList, newList)

                symbolTable.getSymbol(id).getByIndex(0).getValue().setValue(newList)
            else:
                logError("Semantic error: id \"" + id + "\" is not a list")
        else:
            logError("Semantic error: id \"" + id + "\" not found")

def reportCubeChanges(oldCube, newCube):
    for x in range(len(oldCube)):
        for y in range(len(oldCube[0])):
            for z in range(len(oldCube[0][0])):
                aLedWasChanged = oldCube[x][y][z] != newCube[x][y][z]
                if (aLedWasChanged):
                    turn(x, y, z, newCube[x][y][z])

def replaceAtIndexWithOperator(list, indexes, operator):
    if (len(indexes) == 0):
        return replaceWithOperator(list, operator)
    index = indexes.pop(0)
    list[index] = replaceAtIndexWithOperator(list[index], indexes, operator)
    return list

def replaceWithOperator(element, operator):
    elementIsAList = isinstance(element, type([]))
    if elementIsAList:
        for i in range(len(element)):
            element[i] = replaceWithOperator(element[i], operator)
        return element
    else:
        if (operator == "T"):
            return True
        elif (operator == "F"):
            return False
        # toggle boolean value
        return (not element)
