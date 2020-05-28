
import sys
sys.path.append("..")

from Compiler.DataStructures.symbolTable import *
from Utils import *

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


# Processes and sets an arithmetic operation value to a
# variable id in the symbols table
def numExpression(node, symbolTable, scope, varId):
    if not isReadyForRun():
        expressionAsString = getNumExpressionAsString(node, symbolTable, scope)
        if "!" in expressionAsString:
            logError("Semantic Error: numerical operation assignation failed")
        else:
            value = int(eval(expressionAsString))
            if not symbolTable.hasSymbolByScope(varId, scope):
                newSymbol = Symbol(varId, value, Types.Integer, scope)
                symbolTable.add(newSymbol)
            else:
                oldSymbol = symbolTable.getSymbolByScope(varId, scope)
                if oldSymbol.type != Types.Integer and oldSymbol.type != Types.List:
                    logError("Semantic Error: cannot assign integer to boolean variable \"" + varId + "\"")
                else:
                    oldSymbol.setValue(value)
                    symbolTable.modifySymbol(oldSymbol)

# Processes the arithmetic expression node and returns
# it in plain string format
def getNumExpressionAsString(node, symbolTable, scope):
    left = node.getSon(0)
    center = node.getSon(1)
    right = node.getSon(2)

    if left.name == "(":
        return "(" + getNumExpressionAsString(center, symbolTable, scope) + ")"

    if left.name == "numExpression" and right.name == "numExpression":
        leftValue = getNumExpressionAsString(left, symbolTable, scope)
        rightValue = getNumExpressionAsString(right, symbolTable, scope)
        return leftValue + center.name + rightValue

    if left.name == "numExpression" and right.name == "numValue":
        leftValue = getNumExpressionAsString(left, symbolTable, scope)
        rightValue = processNumValue(right.getSon(0).name, symbolTable, scope)
        return leftValue + center.name + rightValue

    if left.name == "numValue" and right.name == "numExpression":
        leftValue = processNumValue(left.getSon(0).name, symbolTable, scope)
        rightValue = getNumExpressionAsString(right, symbolTable, scope)
        return leftValue + center.name + rightValue

    if left.name == "numValue" and right.name == "numValue":
        leftValue = processNumValue(left.getSon(0).name, symbolTable, scope)
        rightValue = processNumValue(right.getSon(0).name, symbolTable, scope)
        return leftValue + center.name + rightValue
    else:
        return ""

# Processes and returns, as a string, the possible
# values of and arithmetic operation: integer or id.
# In case of the id being linked to a boolean or not
# being in the symbol table returns the string "!"
def processNumValue(value, symbolTable, scope):
    if isinstance(value, int):
        return str(value)
    else:
        id = value
        if verifyHasIdByScope(id, symbolTable, scope):
            value = str(symbolTable.getSymbolByScope(id, scope).getValue())
            if value != "True" and value != "False" and value[0] != "[":
                return value
            else:
                if value == "True" or value == "False":
                    logError("Semantic error: illegal arithmetic operation with boolean " + id)
                elif value[0] == "[":
                    logError("Semantic error: illegal arithmetic operation with list " + id)
                return "!"
        else:
            return "!"

# Processes the nested id list node and returns
# it as a plain string list
def getNestedIdNodesAsList(idNode):
    if idNode.name == "idListOne":
        return [idNode.getSon(0).name]
    else:
        return [idNode.getSon(0).name] + getNestedIdNodesAsList(idNode.getSon(2))

# Processes the nested variable value list node
# and returns it as a plain list of values
def getNestedValueNodesAsList(valueListNode):
    # works just for integers and booleans for now
    value = valueListNode.getSon(0)
    if valueListNode.name == "varValueListOne":
        return [value]
    else:
        return [value] + getNestedValueNodesAsList(valueListNode.getSon(2))
