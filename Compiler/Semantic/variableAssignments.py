
import sys
sys.path.append("..")

from Compiler.DataStructures.symbolTable import *
from Utils import isReadyForRun
from Utils import getTypeByValue

# Variable Types
def ID(value, symbolTable, scope, varID):
    if not isReadyForRun():
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
        logError("Semantic Error: Can't find reference to variable: " + str(value))
        return False

def integer(value, symbolTable, scope, varID):
    if not isReadyForRun():
        if value.hasSons():
            integer(value.getSon(0), symbolTable, scope, varID)
        else:
            tempValue = int(value.getName())
            if not symbolTable.hasSymbolByScope(varID, scope):
                tempSymbol = Symbol(varID, tempValue, Types.Integer, scope)
                symbolTable.add(tempSymbol)
            else:
                tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                if tempSymbol.getType() != Types.Integer:
                    logError("Semantic Error: Value: " + str(tempValue) + " . Doesn't match type for variable " + str(tempSymbol.getID()))
                    return False
                tempSymbol.setValue(tempValue)
                symbolTable.modifySymbol(tempSymbol)

def boolean(value, symbolTable, scope, varID):
    if not isReadyForRun():
        if value.hasSons():
            integer(value.getSon(0), symbolTable, scope, varID)
        else:
            tempValue = bool(value.getName())
            if not symbolTable.hasSymbolByScope(varID, scope):
                tempSymbol = Symbol(varID, tempValue, Types.Boolean, scope)
                symbolTable.add(tempSymbol)
            else:
                tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                if tempSymbol.getType() != Types.Boolean:
                    logError("Semantic Error: Value: " + str(tempValue) + " . Doesn't match type for variable " + str(tempSymbol.getID()))
                    return False
                tempSymbol.setValue(tempValue)
                symbolTable.modifySymbol(tempSymbol)

def numExpression(node, symbolTable, scope, varID):
    print "NumExpression at Semantic/variableAssignments.py, line 62"