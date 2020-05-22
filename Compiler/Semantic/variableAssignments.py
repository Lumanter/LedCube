
import sys
sys.path.append("..")

from Compiler.DataStructures.symbolTable import *

# Variable Types
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