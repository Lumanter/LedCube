from Compiler.DataStructures.symbolTable import Types
from Utils import isReadyForRun
from Utils import getIndexes
from Utils import getListElementByIndex
from semanticAnalysis import statementList
from Compiler.ErrorHandling.ErrorHandler import logError


def ifStatement(node, symbolTable, scope):
    if isReadyForRun():
        comparable = node.getSon(1).getSon(0).getName()
        operator = node.getSon(2).getName()
        value = node.getSon(3).getSon(0).getName()
        if comparable == "indexedId":
            elements = getListIndex(node.getSon(1).getSon(0).getSon(1), [])
            comparable = node.getSon(1).getSon(0).getSon(0).getName()
            if symbolTable.hasSymbolByScope(comparable, scope):
                comparable = symbolTable.getSymbolByScope(comparable, scope)
                ifStatementIterativeAux(node, comparable.getValue(), value, operator, symbolTable, scope, elements)

        elif symbolTable.hasSymbolByScope(comparable, scope):
            comparable = symbolTable.getSymbolByScope(comparable, scope)
            if isinstance(comparable.getValue(), list):
                if isinstance(value, bool):
                    ifStatementIterative(node, comparable.getValue(), value, operator, symbolTable, scope)
                else:
                    logError(str(value) + " Must be boolean")
            elif isinstance(comparable.getValue(), bool):
                if isinstance(value, bool):
                    ifStatementBoolean(node, comparable.getValue(), value, operator, symbolTable, scope)
                else:
                    logError(str(value) + " Must be boolean")
            elif isinstance(comparable.getValue(), int):
                if isinstance(value, int):
                    ifStatementInteger(node, comparable, value, operator, symbolTable, scope)
                else:
                    logError(str(value) + " Must be integer")
            else:
                logError("Comparator type not supported")
        else:
            logError("Symbol not found" + str(comparable))



def getListIndex(indexes, listIndex):
    if indexes.hasSons():
        if indexes.getSon(1).getName() == "indexValue":
            if listIndex == []:
                listIndex.append(indexes.getSon(1).getSon(0).getName())
            return listIndex
        else:
            for match in indexes.getSons():
                if match.getName() == "index":
                    if match.getSon(1).getName() == "indexValue":
                        listIndex.append(match.getSon(1).getSon(0).getName())
                else:
                    pass
            getListIndex(match, listIndex)
    else:
        pass
    return listIndex



def ifStatementIterative(node, comparable, value, operator, symbolTable, scope):
        for boolVariable in comparable:
            if operator == "==":
                if boolVariable == value:
                    statementList(node.getSon(5), symbolTable, scope)
                else:
                    pass
            elif operator == "!=":
                if boolVariable != value:
                    statementList(node.getSon(5), symbolTable, scope)
                else:
                    pass
            else:
                logError(operator + ": Operator not supported in variable " + str(type(value)))



def ifStatementIterativeAux(node, comparable, value, operator, symbolTable, scope, indexList):
    if indexList == []:
        if isinstance(comparable, list):
            ifStatementIterative(node, comparable, value, operator, symbolTable, scope)
        elif isinstance(comparable, bool):
            ifStatementBoolean(node, comparable, value, operator, symbolTable, scope)
    else:
        if isinstance(comparable, list):
            if indexList[0]< len(comparable):
                if isinstance(value, bool):
                    ifStatementIterativeAux(node, comparable[indexList[0]], value, operator, symbolTable, scope, indexList[1:])
                else:
                    logError(str(value) + " Must be boolean")
            else:
                logError("List out of range")
        else:
            logError("List out of range")



def ifStatementBoolean(node, comparable, value, operator, symbolTable, scope):
    if operator == "==":
        if comparable == value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == "!=":
        if comparable != value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    else:
        logError(operator + ": Operator not supported in variable " + str(type(value)))



def ifStatementInteger(node, comparable, value, operator, symbolTable, scope):
    if operator == "==":
        if comparable.getValue() == value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == '<':
        if comparable.getValue() < value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == ">":
        if comparable.getValue() > value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == "<=":
        if comparable.getValue() <= value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == ">=":
        if comparable.getValue() >= value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    elif operator == "!=":
        if comparable.getValue() != value:
            statementList(node.getSon(5), symbolTable, scope)
        else:
            pass
    else:
        logError("Value type not supported")



def forLoop(node, symbolTable, scope):
    if isReadyForRun():
        varID = node.getSon(1).getName()
        iterable = node.getSon(3).getSon(0).getName()
        symbolTable.simpleAdd(varID, 0, Types.Integer, scope)
        if not isinstance(iterable, int):
            iterableValueLength = 0
            if iterable == "indexedId":
                tempNode = node.getSon(3).getSon(0)
                tempListSymbol = symbolTable.getSymbolByScope(tempNode.getSon(0).getName(), scope)
                if tempListSymbol == None:
                    tempListSymbol = symbolTable.getSymbolByScope(tempNode.getSon(0).getName(), "global")
                tempList = tempListSymbol.getValue()
                indexes = getIndexes(tempNode.getSon(1), [], symbolTable, scope)
                iterableValueLength = len(getListElementByIndex(tempList, indexes))
            else:
                iterableValue = symbolTable.getSymbolByScope(iterable, scope)
                if iterableValue == None:
                    iterableValue = symbolTable.getSymbolByScope(node.getSon(3).getSon(0).getName(), "global")
                iterableValueLength = len(iterableValue.getValue())
            Step = 1
            if node.getSon(4).getName() == "STEP":
                Step = node.getSon(5).getName()
            totalCycles = iterableValueLength
            if Step == 1:
                for cycle in range(totalCycles):
                    tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                    tempSymbol.setValue(cycle)
                    symbolTable.modifySymbol(tempSymbol)
                    tempStatementList = node.getSon(5)
                    statementList(tempStatementList, symbolTable, scope)
                symbolTable.eliminateSymbolByScope(varID, scope)
            else:
                cycle = 0
                while cycle < totalCycles:
                    tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                    tempSymbol.setValue(cycle)
                    symbolTable.modifySymbol(tempSymbol)
                    tempStatementList = node.getSon(7)
                    statementList(tempStatementList, symbolTable, scope)
                    cycle += Step
                symbolTable.eliminateSymbolByScope(varID, scope)
        else:
            for cycle in range(iterable):
                tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                tempSymbol.setValue(cycle)
                symbolTable.modifySymbol(tempSymbol)
                tempStatementList = node.getSon(5)
                statementList(tempStatementList, symbolTable, scope)
            symbolTable.eliminateSymbolByScope(varID, scope)
