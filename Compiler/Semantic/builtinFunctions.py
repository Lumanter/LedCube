import sys
sys.path.append("..")
import copy

from Utils import *
from Compiler.CodeProduction.codeGenerator import *
from Compiler.ErrorHandling.ErrorHandler import *
from Compiler.DataStructures.symbolTable import *
from listFunctions import *


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

        elif id == "indexedId":
            id = node.getSon(2).getSon(0).getSon(0).name
            if verifyHasId(id, symbolTable):
                list = symbolTable.getSymbolByScope(id, scope).getValue()
                if verifyIsAList(id, list):
                    indexNode = node.getSon(2).getSon(0).getSon(1)
                    indexes = getIndexes(indexNode, [], symbolTable, scope)
                    if verifyIndexesInBounds(id, list, indexes):
                        element = getElementAtIndexes(list, indexes)
                        logPrint(str(element) + "\n")


        else:
            if verifyHasId(id, symbolTable):
                value = symbolTable.getSymbolByScope(id, scope).getValue()
                logPrint(str(value) + "\n")
