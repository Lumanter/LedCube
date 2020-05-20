
from Utils import isReadyForRun


def ifStatement(node, symbolTable, scope):
    if isReadyForRun():
        print "If Statement, I am in Semantic/flowControl, line 5"

def forLoop(node, symbolTable, scope):
    if isReadyForRun():
        print "For Loop, I am in Semantic/flowControl, line 9"
