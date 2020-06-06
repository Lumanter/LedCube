
from Utils import *
from Compiler.CodeProduction.codeGenerator import *
from Compiler.ErrorHandling.ErrorHandler import *
from Compiler.DataStructures.symbolTable import *

# T, F and Neg Operations
def listOperation(node, symbolTable, scope):
    if isReadyForRun():
        id = node.getSon(0).getSon(0).getName()

        if verifyHasId(id, symbolTable):
            oldList = symbolTable.getSymbolByScope(id, scope).getValue()

            if verifyIsAList(id, oldList):
                newList = copy.deepcopy(oldList)

                listOperationWithIndex = (node.getSon(0).getSon(2).getName() == '.')

                if (listOperationWithIndex):
                    indexes = getIndexes(node.getSon(0).getSon(1), [], symbolTable, scope)

                    if indexes[0] == "x,y":
                        indexes = [0, 0]
                        indexes[0] = symbolTable.getSymbolByScope("x", scope).getValue()
                        indexes[1] = symbolTable.getSymbolByScope("y", scope).getValue()


                    if verifyIndexesInBounds(id, oldList, indexes):
                        listOperator = node.getSon(0).getSon(3).getName()
                        replaceAtIndexesWithOperator(newList, indexes, listOperator)

                else :
                    listOperator = node.getSon(0).getSon(2).getName()
                    replaceWithOperator(newList, listOperator)

                if (id == "Cubo"):
                    reportCubeChanges(oldList, newList)

                symbolTable.getSymbolByScope(id, scope).setValue(newList)


def replaceAtIndexesWithOperator(list, indexes, operator):
    if (len(indexes) == 0):
        return replaceWithOperator(list, operator)

    index = indexes.pop(0)
    index = ''.join(str(index).split())

    # [a,b]
    if "," in index:
        subIndexes = splitIndexBySymbol(index, ",")

        # [:,int] column at int
        if subIndexes[0] == ":":
            columnIndex = subIndexes[1]
            for i in range(len(list)):
                list[i][columnIndex] = replaceAtIndexesWithOperator(list[i][columnIndex], indexes, operator)

        #[int, int]
        else:
            list[subIndexes[0]][subIndexes[1]] = replaceAtIndexesWithOperator(list[subIndexes[0]][subIndexes[1]], indexes, operator)

    # [a:b]
    elif ":" in index:
        subIndexes = splitIndexBySymbol(index, ":")
        # [:a] or [a:]
        if len(subIndexes) == 1:
            if index[0] == ":":
                list[:subIndexes[0]] = replaceAtIndexesWithOperator(list[:subIndexes[0]], indexes, operator)
            else:
                list[subIndexes[0]:] = replaceAtIndexesWithOperator(list[subIndexes[0]:], indexes, operator)
        #[a:b]
        else:
            list[subIndexes[0]:subIndexes[1]] = replaceAtIndexesWithOperator(list[subIndexes[0]:subIndexes[1]], indexes, operator)

    # [a]
    else:
        list[int(index)] = replaceAtIndexesWithOperator(list[int(index)], indexes, operator)

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


# Range function to generate lists
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
            appendAtEnd = (index == -1)
            if appendAtEnd:
                list.append(value)
            else:
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
                if isAList(value):
                    for i in range(len(value)):
                        indexInListRange = i < len(matrix)
                        if indexInListRange:
                            listVerifyAndInsert(id, matrix[i], value[i], index)
                else:
                    logError("Semantic Error: Cannot insert single value \"" + str(value) + "\" as a column, list required")

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


# List Len
def lenValue(node, symbolTable, scope, varId):
    if not isReadyForRun():
        lenValue = getLenValue(node, symbolTable, scope)
        if lenValue != -1:
            newSymbol = Symbol(varId, lenValue, Types.Integer, scope)
            symbolTable.add(newSymbol)
