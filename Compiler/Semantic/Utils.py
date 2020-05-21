
import sys
sys.path.append("..")
import os

from ErrorHandling.ErrorHandler import logError

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

def resolveIndexes(indexes, symbolTable, scope):
    for index in range(len(indexes)):
        if not isinstance(indexes[index], int):
            tempSymbol = symbolTable.getSymbolByScope(indexes[index], scope)
            if tempSymbol != None:
                indexes[index] = tempSymbol.getValue()
            else:
                tempSymbol = symbolTable.getSymbolByScope(indexes[index], "global")
                if tempSymbol != None:
                    indexes[index] = tempSymbol.getValue()
                else:
                    print "Can't resolve index " + str(indexes[index]) + " to a value in symbol table"
    return indexes


def getIndexes(indexNode, indexes, symbolTable, scope):
    tempList = indexNode.getSons()
    if len(tempList) == 2:
        for node in tempList:
            indexes = getIndexes(node, indexes, symbolTable, scope)
    else:
        indexes.append(tempList[1].getSon(0).getName())
    return resolveIndexes(indexes, symbolTable, scope)

def getAttributes(functionNode):
    attributes = []
    tempList = functionNode.getSons()[2:-2]
    for attribute in tempList:
        tempName = attribute.getName()
        if tempName != ',':
            attributes.append(tempName)
    return attributes

def verifyIndexBoundries(tempList, indexes):
    if indexes == []:
        return True
    if len(tempList) <= indexes[0]:
        return False
    elif len(indexes) < 2:
        return verifyIndexBoundries(tempList, [])
    else:
        return verifyIndexBoundries(tempList[0], indexes[1:])

def verifyHasId(id, symbolTable):
    if symbolTable.hasSymbol(id):
        return True
    else:
        logError("Semantic error: id \"" + id + "\" not found")

def verifyIsAList(id, list):
    if isAList(list):
        return True
    else:
        logError("Semantic error: id \"" + id + "\" is not a list")
        return False

def verifyIsAMatrix(id, list):
    if verifyIsAList(id, list):
        isAMatrix = all(isinstance(subList, type([])) for subList in list)
        if isAMatrix:
            return True
        else:
            logError("Semantic error: id \"" + id + "\" is not a matrix")
            return False

def verifyIndexInBounds(id, list, index):
    indexBound = len(list) - 1
    indexOutOfRange = index > indexBound or index < 0
    if not indexOutOfRange:
        return True
    else:
        logError("Semantic error: index out of range in list \"" + id + "\"")
        return False

def listElement(element, tempLinkedList):
    tempValue = element.getSon(0)
    if isinstance(tempValue.getName(), bool):
        return tempValue.getName()
    else:
        tempElements = tempValue.getSon(1)
        return listElements(tempElements, [])



def listElements(elements, tempLinkedList):
    tempNodeList = elements.getSons()
    tempLinkedList.append(listElement(tempNodeList[0], tempLinkedList))
    if len(tempNodeList) == 3:
        listElements(tempNodeList[2], tempLinkedList)
    return tempLinkedList

def getListElementByIndex(list, indexes):
    if len(indexes) == 1:
        return list[indexes[0]]
    else:
        return getListElementByIndex(list[indexes[0]], indexes[1:])