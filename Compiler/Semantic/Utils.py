
import sys
sys.path.append("..")
import os
import copy

from Compiler.ErrorHandling.ErrorHandler import logError
from Compiler.CodeProduction.codeGenerator import *

def resetIsReadyForRun():
    file = open(os.path.abspath('..//Compiler//Semantic//runState.txt'), "w")
    file.write("notReady")
    file.close()

def activateIsReadyForRun():
    file = open(os.path.abspath('..//Compiler//Semantic//runState.txt'), "w")
    file.write("ready")
    file.close()

def isReadyForRun():
    file = open(os.path.abspath('..//Compiler//Semantic//runState.txt'), "r")
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
                    if not "," in indexes[index] and not ":" in indexes[index]:
                        logError("Index id \"" + str(indexes[index]) + "\" not found")
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

def verifyIndexesInBounds(id, originalList, indexes):
    indexesInRange = True
    list = copy.deepcopy(originalList)
    for index in indexes:
        if isAList(list):
            if not verifyIndexInBounds(id, list, index):
                indexesInRange = False
                break
            else:
                id += "[" + str(index) + "]"
                list = list[index]
        else:
            indexesInRange = False
            logError("Semantic error: index out of range, element \"" + id + "\" is not a list")
            break
    return indexesInRange

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

def reportCubeChanges(oldCube, newCube):
    for x in range(len(oldCube)):
        for y in range(len(oldCube[0])):
            for z in range(len(oldCube[0][0])):
                aLedWasChanged = oldCube[x][y][z] != newCube[x][y][z]
                if (aLedWasChanged):
                    turn(x, y, z, newCube[x][y][z])

def resetPrintLog():
    file = open(os.path.abspath('..//Compiler//Semantic//prints.txt'), "w")
    file.write("")
    file.close()

def logPrint(message):
    print "Print logged - " + message
    file = open(os.path.abspath('..//Compiler//Semantic//prints.txt'), "a")
    file.write(message)
    file.close()

def getPrints():
    file = open(os.path.abspath(os.path.abspath('..//Compiler//Semantic//prints.txt')), "r")
    prints = ""
    with file:
        prints = file.read()
    file.close()
    return prints

def getIndexesAppendedToId(id, indexes):
    for index in indexes:
        id += "[" +str(index) + "]"
    return id

def getTypeByValue(value):
    from Compiler.DataStructures.symbolTable import Types
    if isinstance(value, bool):
        return Types.Boolean
    if isinstance(value, list):
        return Types.List
    if isinstance(value, int):
        return Types.Integer
    logError("getTypeByValue encounter an unrecognized value" + str(value))

def verifyListsDimensions(list1, list2):
    if not isinstance(list1[0], list) and not isinstance(list2[0], list):
        if len(list1) != len(list2):
            return False
    if not isinstance(list1[0], list):
        return False
    if not isinstance(list2[0], list):
        return False
    elif len(list1) == len(list2):
        for index in range(len(list1)):
            verifyListsDimensions(list1[index], list2[index])
    else:
        return False


# Index Processing Utilities

# Used for splitting index with form [a:b] or [a,b]
def splitIndexBySymbol(index, character):
    indexNumbers = index.split(character)
    # remove empty strings from list from split
    i = 0
    size = len(indexNumbers)
    for iteration in range(size):
        if indexNumbers[i] == "":
            del indexNumbers[i]
        else:
            if indexNumbers[i] != ":":
                indexNumbers[i] = int(indexNumbers[i])
            i += 1
    return indexNumbers


# Returns element given an index with form [a:b]
def processIndexRange(list, indexRange):
    if indexRange == ":":
        return list
    else:
        indexNumbers = splitIndexBySymbol(indexRange, ":")

        if len(indexNumbers) == 1:
            if indexRange[0] == ":":
                return list[:indexNumbers[0]]
            else:
                return list[indexNumbers[0]:]

        else:
            return list[indexNumbers[0]:indexNumbers[1]]


def getColumnAt(matrix, index):
    column = []
    for row in matrix:
        # it's a 3D matrix
        if (isAList(row[index])):
            column.append(row[index][0])
        else:
            column.append(row[index])
    return column


def verifyColumnIsInBounds(id, matrix, index):
    if index < 0:
        return False

    inBounds = True
    for row in matrix:
        if len(row) < index + 1:
            inBounds = False

    if inBounds:
        return True
    else:
        logError("Semantic error: column at \"" + id + "\" out of range")
        return False


# Returns a list's element given a list of indexes
def getElementAtIndexes(list, indexes):
    # shallow copy
    element = list
    for index in indexes:
        # remove white spaces
        index = ''.join(str(index).split())

        # form [a,b]
        if "," in index:
            indexes = splitIndexBySymbol(index, ",")
            # form [:,int] asking for column
            if indexes[0] == ":":
                element = getColumnAt(element, indexes[1])
            # form [int, int]
            else:
                element = element[indexes[0]][indexes[1]]

        # form [a:b]
        elif ":" in index:
            element = processIndexRange(element, index)

        # form [a]
        else:
            element = element[int(index)]

    return element


def verifyIndexInBounds(id, list, index):
    index = ''.join(str(index).split())

    # form [a,b]
    if "," in index:
        indexes = splitIndexBySymbol(index, ",")
        # form [:,int] asking for column
        if indexes[0] == ":":
            id += "[" + str(index) + "]"
            return verifyColumnIsInBounds(id, list, indexes[1])

        # form [int, int]
        else:
            if verifyIndexInBounds(id, list, indexes[0]):
                id += "[" + str(indexes[0]) + "]"
                if verifyIsAList(id, list[int(index[0])]):
                    return verifyIndexInBounds(id, list[int(indexes[0])], int(indexes[1]))
                else:
                    return False
            else:
                return False

    # form [a:b]
    elif ":" in index:
        if processIndexRange(list, index) != []:
            return True
        else:
            id += "[" + index + "]"
            logError("Semantic error: index out of range at \"" + id + "\"")

    # form [a]
    else:
        index = int(index)
        indexBound = len(list) - 1
        indexOutOfRange = index > indexBound or index < 0
        if not indexOutOfRange:
            return True
        else:
            id += "[" + str(index) + "]"
            logError("Semantic error: index out of range at \"" + id + "\"")
            return False


def verifyIndexesInBounds(id, originalList, indexes):
    indexesInRange = True
    list = copy.deepcopy(originalList)
    for index in indexes:
        if isAList(list):
            if not verifyIndexInBounds(id, list, index):
                indexesInRange = False
                break
            else:
                id += "[" + str(index) + "]"
                list = getElementAtIndexes(list, [index])
        else:
            indexesInRange = False
            logError("Semantic error: index out of range, element \"" + id + "\" is not a list")
            break
    return indexesInRange

