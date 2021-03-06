
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode


def p_varAssignment(p):
    '''varAssignment : simpleAssignment
                     | indexAssignment
                     | multipleDeclaration'''
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
                  | ID
                  | indexPair
                  | indexRange'''
    p[0] = ASTNode("indexValue", ([p[1]]))

def p_indexPairId(p):
    'indexPair : ID COMMA ID'
    p[0] = str(p[1]) + p[2] + str(p[3])

def p_indexPair(p):
    'indexPair : INTEGER COMMA INTEGER'
    p[0] = str(p[1]) + p[2] + str(p[3])

def p_indexPair_column(p):
    'indexPair : COLON COMMA INTEGER'
    p[0] = p[1] + p[2] + str(p[3])

def p_indexRange(p):
    'indexRange : INTEGER COLON INTEGER'
    p[0] = str(p[1]) + p[2] + str(p[3])

def p_indexRange_fromStart(p):
    'indexRange : COLON INTEGER'
    p[0] = p[1] + str(p[2])

def p_indexRange_toEnd(p):
    'indexRange : INTEGER COLON'
    p[0] = str(p[1]) + p[2]


def p_varValue(p):
    '''varValue : ID
                | indexedId
                | INTEGER
                | numExpression
                | idNegation
                | BOOLEAN
                | list
                | listDimension
                | listRange
                | len'''
    p[0] = ASTNode("varValue", ([p[1]]))


def p_multipleDeclaration(p):
    'multipleDeclaration : ID COMMA idList ASSIGN varValue COMMA varValueList SEMICOLON'
    p[0] = ASTNode("multipleDeclaration", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))

def p_idList_one(p):
    'idList : ID'
    p[0] = ASTNode("idListOne", [p[1]])

def p_idList_many(p):
    'idList : ID COMMA idList'
    p[0] = ASTNode("idListMany", (p[1], p[2], p[3]));

def p_varValueList_one(p):
    'varValueList : varValue'
    p[0] = ASTNode("varValueListOne", [p[1]])

def p_varValueList_many(p):
    'varValueList : varValue COMMA varValueList'
    p[0] = ASTNode("varValueListMany", (p[1], p[2], p[3]))