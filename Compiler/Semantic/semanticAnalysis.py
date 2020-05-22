import sys
sys.path.append("..")
from Compiler.DataStructures.symbolTable import *
from codeRunner import searchNodeByName
from Compiler.CodeProduction.codeGenerator import *
from Utils import *
from Compiler.ErrorHandling.ErrorHandler import *

from configurationConstants import *
from builtinFunctions import *
from variableAssignments import *

code = None

def findVariables(tree):
    global code
    code = tree
    wipeCode()
    resetIsReadyForRun()
    symbolTable = SymbolTable()
    children = tree.getSons()
    if not processConfigConstants(children[0], symbolTable):
        return False
    if not processVariables(children[1], symbolTable):
        return False
    processSimulationOfCode(children[1], symbolTable)
    #readFinalCode()


def processSimulationOfCode(tree, symbolTable):
    activateIsReadyForRun()

    tempNode = searchNodeByName(tree, "Main")
    procedureDeclaration(tempNode, symbolTable)


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
    if isReadyForRun():
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

def statement(node, symbolTable, scope):
    tempNode = node.getSon(0)

    if tempNode.getName() == "printStatement":
        printStatement(tempNode, symbolTable)
    if tempNode.getName() == "procedureDeclaration":
        procedureDeclaration(tempNode, symbolTable)
    if tempNode.getName() == "varAssignment":
        varAssignment(tempNode, symbolTable, scope)
    if tempNode.getName() == "procedureCall":
        procedureCall(tempNode, symbolTable)
    if tempNode.getName() == "ifStatement":
        from flowControl import ifStatement
        ifStatement(tempNode, symbolTable, scope)
    if tempNode.getName() == "forLoop":
        from flowControl import forLoop
        forLoop(tempNode, symbolTable, scope)
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


def list_process(valueNode, symbolTable, scope, varID):
    elements = valueNode.getSon(1)
    newValue = listElements(elements, [])
    tempSymbol = Symbol(varID, newValue, Types.List, scope)
    symbolTable.modifySymbol(tempSymbol)


def varValue(valueNode, symbolTable, scope, varID):
    value = valueNode.getSon(0)
    varValueType = value.getName()
    if varValueType == "list":
        list_process(value, symbolTable, scope, varID)
    elif varValueType == "listRange":
        listRange(value, symbolTable, scope, varID)
    elif varValueType == "listDimension":
        listDimension(varID, value, symbolTable, scope)
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
    if isReadyForRun():
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