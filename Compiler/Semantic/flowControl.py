from Compiler.DataStructures.symbolTable import Types
from Utils import isReadyForRun
from Utils import getIndexes
from Utils import getListElementByIndex
from semanticAnalysis import statementList


def ifStatement(node, symbolTable, scope):
    if isReadyForRun():
        comparable = node.getSon(1).getSon(0).getName()
        operator = node.getSon(2).getName()
        value = node.getSon(3).getSon(0).getName()
        if (symbolTable.hasSymbolByScope(comparable, scope)):
            comparable = symbolTable.getSymbolByScope(comparable, scope)
            if isinstance(value, bool):
                if operator == "==":
                    if comparable.getValue() == value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == "!=":
                    if comparable.getValue() != value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                else:
                    print "Operator not supported to this variable type"
            elif isinstance(value, int):
                if operator == "==":
                    if comparable.getValue() == value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == '<':
                    if comparable.getValue() < value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == ">":
                    if comparable.getValue() > value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == "<=":
                    if comparable.getValue() <= value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == ">=":
                    if comparable.getValue() >= value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                elif operator == "!=":
                    if comparable.getValue() != value:
                        statementList(node.getSon(5), symbolTable, scope)
                    else:
                        print "Condition not accepted"
                else:
                    print "Value type not supported"

            else:
                print "Comparator type not supported"
        else:
            print "Symbol not found"


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
