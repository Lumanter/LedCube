import sys
sys.path.append("..")
from DataStructures.symbolTable import *
from codeRunner import searchNodeByName
from CodeProduction.codeGenerator import *
from Utils import createCube
from ErrorHandling.ErrorHandler import *

readyForRun = False
code = None


def findVariables(tree):
    global code
    global readyForRun
    code = tree
    wipeCode()
    readyForRun = False
    symbolTable = SymbolTable()
    children = tree.getSons()
    if not processConfigConstants(children[0], symbolTable):
        return False
    if not processVariables(children[1], symbolTable):
        return False
    processSimulationOfCode(children[1], symbolTable)
    readFinalCode()


def processSimulationOfCode(tree, symbolTable):
    global readyForRun
    readyForRun = True

    tempNode = searchNodeByName(tree, "Main")
    procedureDeclaration(tempNode, symbolTable)


def processConfigConstants(configBranch, symbolTable):
    lookupList = ['timer', 'timeUnit', 'rows', 'columns', 'cube']
    for son in configBranch.getSons():
        for keyword in lookupList:
            name = son.getName()
            if name == "cube":
                tempValue = createCube(3, 8, False)
                tempSymbol = Symbol(son.getSon(0).getName(), tempValue, "Reserved", "global")
                symbolTable.add(tempSymbol)
                break
            elif name == keyword:
                tempValue = son.getSons()[2].getName()
                tempSymbol = Symbol(son.getName(), tempValue, "Reserved", "global")
                symbolTable.add(tempSymbol)
                break
            elif keyword == lookupList[-1]:
                return False
    return True


def processVariables(statementBranch, symbolTable):
    scope = "global"

    for node in statementBranch.getSons():
        if node.getName() == "procedureDeclaration":
            procedureDeclaration(node, symbolTable)
        elif node.getName() == "varAssignment":
            varAssignment(node, symbolTable, scope)
        elif node.hasSons():
            processVariables(node, symbolTable)

    return True


def procedureCall(node, symbolTable):
    if readyForRun:
        global code
        tempCode = code.getSons()[1]
        functionName = node.getSon(1).getName()
        tempNode = searchNodeByName(tempCode, functionName)
        valuesParameters = getArguments(node.getSon(3), [])
        parameters = getArguments(tempNode.getSon(3), [])
        symbolTableAdder(parameters, valuesParameters, symbolTable, node.getSon(1).getName())
        procedureDeclaration(tempNode, symbolTable)


def symbolTableAdder(parameters, values, symbolTable, scope):
    for i in range(0, len(parameters)):
        if not (symbolTable.hasSymbolByScope(parameters[i], scope)):
            tempType = Types.Undefined
            if isinstance(values[i], int):
                tempType = Types.Integer
            if isinstance(values[i], bool):
                tempType = Types.Boolean
            if isinstance(values[i], list):
                tempType = Types.List
            symbolTable.add(Symbol(parameters[i], values[i], tempType, scope))
        else:
            variable = symbolTable.getSymbolByScope(parameters[i], scope)
            variable.setValue(values[i])
            symbolTable.modifySymbol(variable)


def getArgumentsAux(argumentNode, arguments):
    if argumentNode.getName() == "argument":
        arguments.append(argumentNode.getSon(0).getSon(0).getName())
    elif argumentNode.getName() == "parameter":
        arguments.append(argumentNode.getSon(0).getName())
    else:
        getArguments(argumentNode, arguments)


def getArguments(argumentNode, arguments):
    tempList = argumentNode.getSons()
    for node in tempList:
        if node.getName() != ',':
            getArgumentsAux(node, arguments)
    return arguments


def getAttributes(functionNode):
    attributes = []
    tempList = functionNode.getSons()[2:-2]
    for attribute in tempList:
        tempName = attribute.getName()
        if tempName != ',':
            attributes.append(tempName)
    return attributes


def delayFunction(tempNode, symbolTable):
    if readyForRun:
        attributes = getAttributes(tempNode)
        if len(attributes) != 0:
            delay(attributes[0], attributes[1])
        else:
            tempSymbolTime = symbolTable.getSymbol("timer").getByIndex(0).getValue()
            tempSymbolTimeUnit = symbolTable.getSymbol("timeUnit").getByIndex(0).getValue()
            delay(str(tempSymbolTime.getValue()), str(tempSymbolTimeUnit.getValue()))


def defaultCode(tempNode, symbolTable):
    if readyForRun:
        attributes = getAttributes(tempNode)
        cubeValue = createCube(3, 6, attributes)
        tempCubeSymbol = symbolTable.getSymbolByScope("cube", "global")
        tempCubeSymbol.setValue(cubeValue)
        symbolTable.modifySymbol(tempCubeSymbol)


def builtInFunction(node, symbolTable, scope):
    tempNode = node.getSon(0)
    tempName = tempNode.getName()

    if tempName == "delay":
        delayFunction(tempNode, symbolTable)
    if tempName == "defaultCube":
        defaultCode(tempNode, symbolTable)
    if tempName == "listOperation":
        listOperation(node, symbolTable, scope)


def statement(node, symbolTable, scope):
    tempNode = node.getSon(0)

    if tempNode.getName() == "procedureDeclaration":
        procedureDeclaration(tempNode, symbolTable)
    if tempNode.getName() == "varAssignment":
        varAssignment(tempNode, symbolTable, scope)
    if tempNode.getName() == "procedureCall":
        procedureCall(tempNode, symbolTable)
    if tempNode.getName() == "builtInFunction":
        builtInFunction(tempNode, symbolTable, scope)
        pass


def statementList(node, symbolTable, scope):
    for tempNode in node.getSons():
        if tempNode.getName() == "statement":
            statement(tempNode, symbolTable, scope)
        if tempNode.getName() == "statementList":
            statementList(tempNode, symbolTable, scope)


def procedureDeclaration(node, symbolTable):
    scope = node.getSon(1).getName()

    for tempNode in node.getSons():
        if tempNode.getName() == "statementList":
            statementList(tempNode, symbolTable, scope)


def numExpression(value, symbolTable, scope, varID):
    if value.hasSons():
        numExpression(value.getSon(0), symbolTable, scope, varID)
    else:
        tempValue = int(value.getName())
        if not symbolTable.hasSymbolByScope(varID, scope):
            tempSymbol = Symbol(varID, tempValue, Types.Integer, scope)
            symbolTable.add(tempSymbol)
        else:
            return False


def boolean(value, symbolTable, scope, varID):
    if value.hasSons():
        numExpression(value.getSon(0), symbolTable, scope, varID)
    else:
        tempValue = bool(value.getName())
        if not symbolTable.hasSymbolByScope(varID, scope):
            tempSymbol = Symbol(varID, tempValue, Types.Integer, scope)
            symbolTable.add(tempSymbol)
        else:
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


def list_process(valueNode, symbolTable, scope, varID):
    elements = valueNode.getSon(1)
    newValue = listElements(elements, [])
    tempSymbol = Symbol(varID, newValue, Types.List, scope)
    symbolTable.modifySymbol(tempSymbol)


def ID(value, symbolTable, scope, varID):
    tempSymbol = symbolTable.getSymbolByScope(value, scope)
    if tempSymbol != None:
        tempValue = tempSymbol.getValue()
        tempNewSymbol = Symbol(varID, tempValue, tempSymbol.getType(), scope)
        symbolTable.modifySymbol(tempNewSymbol)
        return True
    tempSymbol = symbolTable.getSymbolByScope(value, "global")
    if tempSymbol != None:
        tempValue = tempSymbol.getValue()
        tempNewSymbol = Symbol(varID, tempValue, tempSymbol.getType(), scope)
        symbolTable.modifySymbol(tempNewSymbol)
        return True
    return False


def varValue(valueNode, symbolTable, scope, varID):
    value = valueNode.getSon(0)
    varValueType = value.getName()
    if varValueType == "list":
        list_process(value, symbolTable, scope, varID)
    elif type(True) == type(value.getName()):
        boolean(value, symbolTable, scope, varID)
    elif isinstance(varValueType, int):
        numExpression(value, symbolTable, scope, varID)
    else:
        ID(varValueType, symbolTable, scope, varID)


def simpleAssignment(tempNode, symbolTable, scope):
    varID = tempNode.getSon(0).getName()
    valueNode = tempNode.getSon(2)
    varValue(valueNode, symbolTable, scope, varID)


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


def indexVarValue(valueNode, symbolTable, scope):
    value = valueNode.getSon(0)
    if type(True) == type(value.getName()):
        return value.getName()
    else:
        tempSymbol = symbolTable.getSymbolByScope(value.getName(), scope)
        tempValue = tempSymbol.getValue()
        return tempValue


def changeValueInList(lista, indexes, value):
    if not isinstance(lista[0], list):
        lista[indexes[0]] = value
    else:
        if indexes[0] < len(lista):
            changeValueInList(lista[indexes[0]], indexes[1:], value)
        else:
            print "Error in function changeValueInList: " + str(
                indexes[0]) + " is bigger than the size of the dimensions of the list or matrix"


def verifyIndexBoundries(tempList, indexes):
    if indexes == []:
        return True
    if len(tempList) <= indexes[0]:
        return False
    elif len(indexes) < 2:
        return verifyIndexBoundries(tempList, [])
    else:
        return verifyIndexBoundries(tempList[0], indexes[1:])


def modifySymbolList(tempID, tempIndex, tempValue, scope, symbolTable):
    tempSymbol = symbolTable.getSymbolByScope(tempID, scope)
    if tempSymbol != None:
        tempList = tempSymbol.getValue()
        if verifyIndexBoundries(tempList, tempIndex):
            changeValueInList(tempList, tempIndex, tempValue)
            return True
        else:
            print "Error in modifySymbolList: indexes out of range"
            return False
    tempSymbol = symbolTable.getSymbolByScope(tempID, "global")
    if tempSymbol != None:
        tempList = tempSymbol.getValue()
        if verifyIndexBoundries(tempList, tempIndex):
            changeValueInList(tempList, tempIndex, tempValue)
            return True



def indexAssignment(tempNode, symbolTable, scope):
    if readyForRun:
        tempID = tempNode.getSon(0).getName()
        tempIndex = getIndexes(tempNode.getSon(1), [], symbolTable, scope)
        tempValue = indexVarValue(tempNode.getSon(3), symbolTable, scope)

        if not modifySymbolList(tempID, tempIndex, tempValue, scope, symbolTable):
            return False
        if tempID.lower() == "cubo" or tempID.lower() == "cube":
            turn(tempIndex[0], tempIndex[1], tempIndex[2], tempValue)


def varAssignment(node, symbolTable, scope):
    tempNode = node.getSons()[0]
    if tempNode.getName() == "simpleAssignment":
        simpleAssignment(tempNode, symbolTable, scope)
    if tempNode.getName() == "indexAssignment":
        indexAssignment(tempNode, symbolTable, scope)

def listOperation(node, symbolTable, scope):
    if (readyForRun):

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

def isAList(list):
    return isinstance(list, type([]))

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
