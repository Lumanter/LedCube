
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode


def p_varAssignment(p):
    '''varAssignment : simpleAssignment
                     | indexAssignment'''
    p[0] = ASTNode("varAssignment", [p[1]])


def p_simpleAssignment(p):
    'simpleAssignment : ID ASSIGN varValue SEMICOLON'
    p[0] = ASTNode("simpleAssignment", (p[1], p[2], p[3], p[4]))


def p_indexAssignment(p):
    'indexAssignment : ID index ASSIGN varValue SEMICOLON'
    p[0] = ASTNode("indexAssignment", (p[1], p[2], p[3], p[4], p[5]))

def p_indexedId(p):
    'indexedId : ID index'
    p[0] = ASTNode("indexedId", (p[1], p[2]))

def p_indexOne(p):
    'index : LSQUAREBRACKET indexValue RSQUAREBRACKET'
    p[0] = ASTNode("index", (p[1], p[2], p[3]))


def p_indexMany(p):
    'index : index index'
    p[0] = ASTNode("index", (p[1], p[2]))


def p_indexValue(p):
    '''indexValue : INTEGER 
                  | ID'''
    p[0] = ASTNode("indexValue", ([p[1]]))


def p_varValue(p):
    '''varValue : ID
                | numExpression 
                | BOOLEAN
                | list
                | listDimension
                | listRange'''
    p[0] = ASTNode("varValue", ([p[1]]))