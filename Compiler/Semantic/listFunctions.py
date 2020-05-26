
from Utils import *
from Compiler.CodeProduction.codeGenerator import *
from Compiler.ErrorHandling.ErrorHandler import *
from Compiler.DataStructures.symbolTable import *

# T, F and Neg Operations
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


# List Shape/Dimension functions
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
    if dimensionType == "shapeF":
        columns = len(matrix)
        return columns
    elif dimensionType == "shapeC":
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
