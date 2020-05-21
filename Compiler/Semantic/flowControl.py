from Compiler.DataStructures.symbolTable import Types
from Utils import isReadyForRun
from semanticAnalysis import statementList


def ifStatement(node, symbolTable, scope):
    if isReadyForRun():
        print "If Statement, I am in Semantic/flowControl, line 5"


def forLoop(node, symbolTable, scope):
    if isReadyForRun():
        varID = node.getSon(1).getName()
        iterable = node.getSon(3).getSon(0).getName()
        symbolTable.simpleAdd(varID, 0, Types.Integer, scope)
        if not isinstance(iterable, int):
            iterableValue = symbolTable.getSymbolByScope(iterable, scope)
            if iterableValue == None:
                iterableValue = symbolTable.getSymbolByScope(node.getSon(3).getSon(0).getName(), "global")
            Step = 1
            if node.getSon(4).getName() == "STEP":
                Step = node.getSon(5).getName()
            totalCycles = len(iterableValue.getValue())
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
