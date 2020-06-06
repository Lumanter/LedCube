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
    if tempName == "blink":
        blinkNode(node, symbolTable, scope)

# Delay
def delayFunction(tempNode, symbolTable):
    if isReadyForRun():
        attributes = getAttributes(tempNode)
        if len(attributes) != 0:
            delay(attributes[0], attributes[1])
        else:
            tempSymbolTime = symbolTable.getSymbol("timer").getByIndex(0).getValue()
            tempSymbolTimeUnit = symbolTable.getSymbol("timeUnit").getByIndex(0).getValue()
            if (str(tempSymbolTimeUnit.getValue()) == "Nada"):
                logError("Semantic error: can't do default delay with rango_timer value \"Nada\"")
            else:
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

        elif id == "len":
            lenNode = node.getSon(2).getSon(0)
            lenValue = getLenValue(lenNode, symbolTable, scope)
            if lenValue != -1:
                logPrint(str(lenValue) + "\n")

        else:
            if verifyHasId(id, symbolTable):
                value = symbolTable.getSymbolByScope(id, scope).getValue()
                logPrint(str(value) + "\n")


# Blink
def blinkNode(node, symbolTable, scope):
    node = node.getSon(0)
    if isReadyForRun():
        id = node.getSon(2).getSon(0).name
        if verifyHasIdByScope(id, symbolTable, scope):

            if id == "Cubo":
                cubo = symbolTable.getSymbolByScope(id, scope).getValue()
                indexNode = node.getSon(2).getSon(1)
                indexes = getIndexes(node.getSon(2).getSon(1), [], symbolTable, scope)
                time = ""
                timeUnit = ""
                state = "True"
                if verifyIndexesInBounds(id, cubo, indexes):

                    customBlink = len(node.sonList) > 6
                    if customBlink:
                        time = node.getSon(4).name
                        timeUnit = node.getSon(6).name
                        state = node.getSon(8).name
                    else:
                        time = symbolTable.getSymbol("timer").getByIndex(0).getValue().getValue()
                        timeUnit = symbolTable.getSymbol("timeUnit").getByIndex(0).getValue().getValue()
                        state = node.getSon(4).name

                    blinkIndexes(indexes, time, timeUnit, state)

            else:
                logPrint("Blink function only has effect on variable \"Cubo\"")

def blinkIndexes(indexes, time, timeUnit, state):
    if len(indexes) == 3:
        blink(indexes[0], indexes[1], indexes[2], time, timeUnit, state)

    if len(indexes) == 2:
        for z in range(8):
            blink(indexes[0], indexes[1], z, time, timeUnit, state)

    if len(indexes) == 1:
        for y in range(8):
            for z in range(8):
                blink(indexes[0], y, z, time, timeUnit, state)