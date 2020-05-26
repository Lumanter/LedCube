import sys
sys.path.append("..")
import copy

from Utils import *
from Compiler.CodeProduction.codeGenerator import *
from Compiler.ErrorHandling.ErrorHandler import *
from Compiler.DataStructures.symbolTable import *


def builtInFunction(node, symbolTable, scope):
    tempNode = node.getSon(0)
    tempName = tempNode.getName()

    if tempName == "delay":
        delayFunction(tempNode, symbolTable)
    if tempName == "defaultCube":
        defaultCode(tempNode, symbolTable)
    if tempName == "listOperation":
        listOperation(node, symbolTable, scope)
    if tempName == "listInsert":
        listInsert(node, symbolTable, scope)
    if tempName == "matrixInsert":
        matrixInsert(node, symbolTable, scope)
    if tempName == "listDelete":
        listDelete(node, symbolTable, scope)
    if tempName == "matrixDelete":
        matrixDelete(node, symbolTable, scope)

# Delay
def delayFunction(tempNode, symbolTable):
    if isReadyForRun():
        attributes = getAttributes(tempNode)
        if len(attributes) != 0:
            delay(attributes[0], attributes[1])
        else:
            tempSymbolTime = symbolTable.getSymbol("timer").getByIndex(0).getValue()
            tempSymbolTimeUnit = symbolTable.getSymbol("timeUnit").getByIndex(0).getValue()
            delay(str(tempSymbolTime.getValue()), str(tempSymbolTimeUnit.getValue()))


# Default Cube
def defaultCode(tempNode, symbolTable):
    if isReadyForRun():
        attributes = getAttributes(tempNode)
        cubeValue = createCube(3, 6, attributes)
        tempCubeSymbol = symbolTable.getSymbolByScope("cube", "global")
        tempCubeSymbol.setValue(cubeValue)
        symbolTable.modifySymbol(tempCubeSymbol)


# List T, F, Neg Operations
def listOperation(node, symbolTable, scope):
    if isReadyForRun():
        id = node.getSon(0).getSon(0).getName()

        if symbolTable.hasSymbol(id):
            oldList = symbolTable.getSymbolByScope(id, scope).getValue()

            if isAList(oldList):
                newList = copy.deepcopy(oldList)

                listOperationWithIndex = (node.getSon(0).getSon(2).getName() == '.')
                if (listOperationWithIndex):
                    indexes = getIndexes(node.getSon(0).getSon(1), [], symbolTable, scope)
                    indexOutOfRange = not verifyIndexBoundries(oldList, indexes)
                    if not indexOutOfRange:
                        listOperator = node.getSon(0).getSon(3).getName()
                        replaceAtIndexWithOperator(newList, indexes, listOperator)
                    else:
                        logError("Semantic error: index out of range in \"" + id + "\"")
                else :
                    listOperator = node.getSon(0).getSon(2).getName()
                    replaceWithOperator(newList, listOperator)

                if (id == "Cubo"):
                    reportCubeChanges(oldList, newList)

                symbolTable.getSymbolByScope(id, scope).setValue(newList)
            else:
                logError("Semantic error: id \"" + id + "\" is not a list")
        else:
            logError("Semantic error: id \"" + id + "\" not found")

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
        return (not element)


# List Dimension
def listDimension(varID, node, symbolTable, scope):
    listId = node.getSon(0).name
    if symbolTable.hasSymbol(listId):

        list = symbolTable.getSymbolByScope(listId, scope).getValue()
        if isAList(list):

            isAMatrix = all(isinstance(subList, type([])) for subList in list)
            if isAMatrix:
                dimensionType = node.getSon(1).name
                dimensionValue = getDimension(list, dimensionType)
                newSymbol = Symbol(varID, dimensionValue, Types.Integer, scope)
                symbolTable.add(newSymbol)
            else:
                logError("Semantic error: " + listId + " is not matrix")
        else:
            logError("Semantic error: id \"" + listId + "\" is not a list")
    else:
        logError("Semantic error: id \"" + listId + "\" not found")

def getDimension(matrix, dimensionType):
    if dimensionType == "shapeC":
        columns = len(matrix)
        return columns
    elif dimensionType == "shapeF":
        if isinstance(matrix[0], type([])):
            rows = len(matrix[0])
            return rows
        else:
            logError("Semantic error: cannot get shape F of a list that has less than 2 dimensions")
            return 0
    else:
        if isinstance(matrix[0][0], type([])):
            depth = len(matrix[0][0])
            return depth
        else:
            logError("Semantic error: cannot get shape A of a list that has less than 3 dimensions")
            return 0


# List Range
def listRange(node, symbolTable, scope, varID):
    size = node.getSon(4).name
    value = node.getSon(6).name
    generatedList = [value] * size
    newSymbol = Symbol(varID, generatedList, Types.List, scope)
    symbolTable.add(newSymbol)


# List Insert
def listInsert(node, symbolTable, scope):
    if isReadyForRun():

        id = node.getSon(0).getSon(0).name
        if verifyHasId(id, symbolTable):

            list = symbolTable.getSymbolByScope(id, scope).getValue()
            value = processInsertValue(node.getSon(0).getSon(6).getSon(0))

            index = node.getSon(0).getSon(4).name
            listVerifyAndInsert(id, list, value, index)

def listVerifyAndInsert(id, list, value, index):
    if not id == "Cubo":
        if verifyIsAList(id, list):
            if verifyIndexInBounds(id, list, index):
                list.insert(index, value)
    else:
        logError("Semantic Error: Cube variable doesn't support list insert function")

# Matrix Insert
def matrixInsert(node, symbolTable, scope):
    if isReadyForRun():
        id = node.getSon(0).getSon(0).name
        if not id == "Cubo":
            if verifyHasId(id, symbolTable):
                matrix = symbolTable.getSymbolByScope(id, scope).getValue()
                value = processInsertValue(node.getSon(0).getSon(4).getSon(0))
                index = node.getSon(0).getSon(8).name
                insertAsColumn = node.getSon(0).getSon(6).name
                matrixVerifyAndInsert(id, matrix, value, index, insertAsColumn)
        else:
            logError("Semantic Error: Cube variable doesn't support matrix insert function")

def matrixVerifyAndInsert(id, matrix, value, index, insertAsColumn):
    if insertAsColumn == 0 or insertAsColumn == 1:
        if insertAsColumn:
            if verifyIsAMatrix(id, matrix):
                for i in range(len(value)):
                    indexInListRange = i < len(matrix)
                    if indexInListRange:
                        listVerifyAndInsert(id, matrix[i], value[i], index)

        else:
            listVerifyAndInsert(id, matrix, value, index)
    else:
        logError("Semantic error: attempted insert with type illegal value, change to 0 for rows or 1 for columns")

def processInsertValue(node):
    if node.name == "list":
        processedList = listElements(node.getSon(1), [])
        return processedList
    else:
        return node.name

# List Delete
def listDelete(node, symbolTable, scope):
    if isReadyForRun():

        id = node.getSon(0).getSon(0).name
        idIndexNode = node.getSon(0).getSon(1)
        deleteIndex = node.getSon(0).getSon(5).name
        listVerifyAndDelete(id, symbolTable, idIndexNode, deleteIndex, scope)

def listVerifyAndDelete(id, symbolTable, idIndexNode, deleteIndex, scope):
    if verifyHasId(id, symbolTable):

        list = symbolTable.getSymbolByScope(id, scope).getValue()
        if verifyIsAList(id, list):

            idHasIndexes = idIndexNode.name != ""
            if idHasIndexes:
                indexes = getIndexes(idIndexNode, [], symbolTable, scope)
                if verifyIndexesInBounds(id, list, indexes):
                    list = getElementAtIndexes(list, indexes)
                    id = getIndexesAppendedToId(id, indexes)
                    if verifyIsAList(id, list):
                        if verifyIndexInBounds(id, list, deleteIndex):
                            del list[deleteIndex]
            else:
                if verifyIndexInBounds(id, list, deleteIndex):
                    del list[deleteIndex]

# Matrix Delete
def matrixDelete(node, symbolTable, scope):
    if isReadyForRun():

        id = node.getSon(0).getSon(0).name
        idIndexNode = node.getSon(0).getSon(1)
        deleteIndex = node.getSon(0).getSon(5).name
        deleteColumn = node.getSon(0).getSon(7).name

        if deleteColumn == 0 or deleteColumn == 1:
            if deleteColumn:

                if verifyHasId(id, symbolTable):

                    matrix = symbolTable.getSymbolByScope(id, scope).getValue()
                    if verifyIsAMatrix(id, matrix):

                        idHasIndexes = idIndexNode.name != ""

                        if idHasIndexes:
                            indexes = getIndexes(idIndexNode, [], symbolTable, scope)
                            if verifyIndexesInBounds(id, matrix, indexes):
                                matrix = getElementAtIndexes(matrix, indexes)
                                id = getIndexesAppendedToId(id, indexes)
                                if not verifyIsAMatrix(id, matrix):
                                    return

                        indexInRowsRange = True
                        for row in matrix:
                            if not verifyIndexInBounds(id+ "[" + str(row) + "]", row, deleteIndex):
                                indexInRowsRange = False
                        if indexInRowsRange:
                            deleteColumnAt(matrix, deleteIndex)
            else:
                listVerifyAndDelete(id, symbolTable, idIndexNode, deleteIndex, scope)
        else:
            logError("Semantic error: attempted delete type with illegal value, change to 0 for rows or 1 for columns")

def deleteColumnAt(matrix, index):
    for subMatrix in matrix:
        del subMatrix[index]


# Print Statement
def printStatement(node, symbolTable, scope):
    if isReadyForRun():
        id = node.getSon(2).getSon(0).name
        if id == "type":
            id = node.getSon(2).getSon(0).getSon(2).name
            if verifyHasId(id, symbolTable):
                type = symbolTable.getSymbolByScope(id, scope).type
                type = (str(type)[6:]).lower()
                logPrint(str(type) + "\n")

        else:
            if verifyHasId(id, symbolTable):
                value = symbolTable.getSymbolByScope(id, scope).getValue()
                logPrint(str(value) + "\n")
