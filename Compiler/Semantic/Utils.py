
import os

def resetIsReadyForRun():
    file = open(os.path.abspath('.//Semantic//runState.txt'), "w")
    file.write("notReady")
    file.close()

def activateIsReadyForRun():
    file = open(os.path.abspath('.//Semantic//runState.txt'), "w")
    file.write("ready")
    file.close()

def isReadyForRun():
    file = open(os.path.abspath('.//Semantic//runState.txt'), "r")
    runState = ""
    with file:
        runState = file.read()
    isReadyForRun = (runState == "ready")
    file.close()
    return isReadyForRun

def findNumValue(node):
    if node != None:
        if isinstance(node, int):
            return node
        if isinstance(node.getName(), int):
            return node.getName()
        tempList = node.getSons()
        for tempNode in tempList:
            findNumValue(tempNode)
    pass


def createCube(dimension, size, value):
    cube = []
    if dimension == 1:
        for index in range(size):
            cube.append(value)
    else:
        for index in range(size):
            cube.append(createCube(dimension - 1, size, value))
    return cube

def isAList(list):
    return isinstance(list, type([]))

def getIndexes(indexNode, indexes, symbolTable, scope):
    tempList = indexNode.getSons()
    for node in tempList:
        if node.getSonsLength() == 3:
            tempValue = node.getSon(1).getSon(0).getName()
            if isinstance(tempValue, int):
                indexes.append(tempValue)
            else:
                tempSymbol = symbolTable.getSymbolByScope(tempValue, scope)
                if tempSymbol != None:
                    tempValue = tempSymbol.getValue()
                    indexes.append(tempValue)
                else:
                    tempSymbol = symbolTable.getSymbolByScope(tempValue, "global")
                    if tempSymbol != None:
                        tempValue = tempSymbol.getValue()
                        indexes.append(tempValue)
                    else:
                        print str(tempValue) + "doesn't fit any symbol stored in the symbolTable"
                        return None
        else:
            getIndexes(node, indexes, symbolTable, scope)
    return indexes

def getAttributes(functionNode):
    attributes = []
    tempList = functionNode.getSons()[2:-2]
    for attribute in tempList:
        tempName = attribute.getName()
        if tempName != ',':
            attributes.append(tempName)
    return attributes
