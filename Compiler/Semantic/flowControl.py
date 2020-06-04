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


"""def ifStatementIterativeRangeList(node, comparable, value, operator, symbolTable, scope, indexList):
    if isinstance(indexList[0], str):
        try:
            index = int(indexList[0][2:])
            indexList[0] = index
        except ValueError:
            logError(index + " must be integer type")
        for item in range(0, len(comparable)):
            if len(comparable) > indexList[0]:
                ifStatementBoolean(node, comparable[item][indexList[0]], value, operator, symbolTable, scope)
            else:
                return logError("List out of range")
        return
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
            logError("List out of range")"""


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
    elif isinstance(indexList[0], str):
        try:
            index = int(indexList[0][2:])
            indexList[0] = index
        except ValueError:
            logError(index + " must be integer type")
        try:
            for item in range(0, len(comparable)):
                if len(comparable) > indexList[0]:
                    if isinstance(comparable[item], list):
                        ifStatementBoolean(node, comparable[item][indexList[0]], value, operator, symbolTable, scope)
                    elif isinstance(comparable[item], bool):
                        if item == indexList[0]:
                            ifStatementBoolean(node, comparable[indexList[0]], value, operator, symbolTable, scope)
                    else:
                        return logError(str(comparable[item]) + " Must be list or boolean")

                else:
                    return logError("List out of range")
            return
        except:
            return logError(str(comparable)+" is not iterable")
    else:
        if isinstance(comparable, list):
            if indexList[0] < len(comparable):
                if isinstance(value, bool):
                    ifStatementIterativeAux(node, comparable[indexList[0]], value, operator, symbolTable, scope,
                                            indexList[1:])
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
        isRange = False
        if not isinstance(iterable, int):
            iterableValueLength = 0
            if iterable == "indexedId":
                tempNode = node.getSon(3).getSon(0)
                tempListSymbol = symbolTable.getSymbolByScope(tempNode.getSon(0).getName(), scope)
                if tempListSymbol == None:
                    tempListSymbol = symbolTable.getSymbolByScope(tempNode.getSon(0).getName(), "global")
                tempList = tempListSymbol.getValue()
                indexes = getIndexes(tempNode.getSon(1), [], symbolTable, scope)
                for value in indexes:
                    if not isinstance(value, int):
                        if value[1] == ':':
                            isRange = True
                            forLoopWithRange(node, varID, indexes, symbolTable, scope)
                            break
                    else:
                        break
                if not isRange:
                    iterableValueLength = len(getListElementByIndex(tempList, indexes))
            else:
                iterableValue = symbolTable.getSymbolByScope(iterable, scope)
                if iterableValue == None:
                    iterableValue = symbolTable.getSymbolByScope(node.getSon(3).getSon(0).getName(), "global")
                iterableValueLength = len(iterableValue.getValue())
            if not isRange:
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


def forLoopWithRange(node, varID, indexes, symbolTable, scope):
    Step = 1
    if node.getSon(4).getName() == "STEP":
        Step = node.getSon(5).getName()
    lowerLimit = int(indexes[0][0])
    upperLimit = int(indexes[0][2])
    if lowerLimit < upperLimit:
        if node.getSon(4).getName() == "STEP":
            Step = node.getSon(5).getName()
        totalCycles = upperLimit-lowerLimit
        if Step == 1:
            for cycle in range(lowerLimit, upperLimit):
                tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                tempSymbol.setValue(cycle)
                symbolTable.modifySymbol(tempSymbol)
                tempStatementList = node.getSon(5)
                statementList(tempStatementList, symbolTable, scope)
            symbolTable.eliminateSymbolByScope(varID, scope)
        else:
            cycle = lowerLimit
            while cycle < upperLimit:
                tempSymbol = symbolTable.getSymbolByScope(varID, scope)
                tempSymbol.setValue(cycle)
                symbolTable.modifySymbol(tempSymbol)
                tempStatementList = node.getSon(7)
                statementList(tempStatementList, symbolTable, scope)
                cycle += Step
            symbolTable.eliminateSymbolByScope(varID, scope)
    else:
        logError("Semantic: UpperLimit " + str(upperLimit) + " doesn't match LowerLimit " + str(lowerLimit))

