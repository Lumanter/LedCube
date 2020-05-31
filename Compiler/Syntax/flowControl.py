
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode

# For Loop
def p_forLoop(p):
    'forLoop : FOR ID IN iterable LBRACE statementList RBRACE SEMICOLON'
    p[0] = ASTNode("forLoop", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))

def p_forLoop_step(p):
    'forLoop : FOR ID IN iterable STEP INTEGER LBRACE statementList RBRACE SEMICOLON'
    p[0] = ASTNode("forLoop", (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))

def p_iterable(p):
    '''iterable : ID
                | indexedId
                | INTEGER'''
    p[0] = ASTNode("iterable", [p[1]])


# If Statement
def p_ifStatement(p):
    'ifStatement : IF ifIterable COMPARATOR comparisonValue LBRACE statementList RBRACE SEMICOLON'
    p[0] = ASTNode("ifStatement", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))

def p_ifIterable(p):
    '''ifIterable : ID
                 | indexedId'''
    p[0] = ASTNode("ifIterable", [p[1]])

def p_comparisonValue(p):
    '''comparisonValue : BOOLEAN
                       | INTEGER'''
    p[0] = ASTNode("comparisonValue", [p[1]])
