
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode


def p_builtInFunction(p):
    '''builtInFunction : delay
                       | listOperation
                       | listInsert
                       | matrixInsert
                       | listDelete
                       | matrixDelete
                       | blink'''
    p[0] = ASTNode("builtInFunction", ([p[1]]))


# Delay 
def p_delayDefault(p):
    'delay : DELAY LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = ASTNode("delay", (p[1], p[2], p[3], p[4]))

def p_delayCustom(p):
    'delay : DELAY LPARENTHESES INTEGER COMMA TIMEUNIT RPARENTHESES SEMICOLON'
    p[0] = ASTNode("delay", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))


# Default Cube 
def p_defaultCube(p):
    'list : DEFAULTCUBE LPARENTHESES BOOLEAN RPARENTHESES'
    p[0] = ASTNode("defaultCube", (p[1], p[2], p[3], p[4]))


# List T/F/Neg Operations
def p_listOperation(p):
    'listOperation : ID LISTOPERATOR SEMICOLON'
    p[0] = ASTNode("listOperation", (p[1], '.', p[2]))

def p_listOperation_index(p):
    'listOperation : ID index LISTOPERATOR SEMICOLON'
    p[0] = ASTNode("listOperation", (p[1], p[2], '.', p[3]))

# List Dimension
def p_listDimension(p):
    'listDimension : ID LISTDIMENSION'
    p[0] = ASTNode("listDimension", (p[1], p[2]))


# List Range Function
def p_listRange(p):
    'listRange : LIST LPARENTHESES RANGE LPARENTHESES INTEGER COMMA BOOLEAN RPARENTHESES RPARENTHESES'
    p[0] = ASTNode("listRange", (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))


# List Insert Function
def p_listInsert(p):
    'listInsert : ID INSERT LPARENTHESES INTEGER COMMA insertValue RPARENTHESES SEMICOLON'
    p[0] = ASTNode("listInsert", (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7]))

def p_matrixInsert(p):
    'matrixInsert : ID INSERT LPARENTHESES insertValue COMMA INTEGER COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("matrixInsert", (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))

def p_matrixInsert_noIndex(p):
    'matrixInsert : ID INSERT LPARENTHESES insertValue COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("matrixInsert", (p[1], '.', p[2], p[3], p[4], p[5], p[6], ",", -1, ")"))

def p_insertValue(p):
    '''insertValue : BOOLEAN
                  | list'''
    p[0] = ASTNode("insertValue", [p[1]])

# List Delete Function
def p_listDelete(p):
    'listDelete : ID DELETE LPARENTHESES INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("listDelete", (p[1], "", '.', p[2], p[3], p[4], p[5]))

def p_listDelete_atIdIndex(p):
    'listDelete : ID index DELETE LPARENTHESES INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("listDelete", (p[1], p[2], '.', p[3], p[4], p[5], p[6]))

def p_matrixDelete(p):
    'matrixDelete : ID DELETE LPARENTHESES INTEGER COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("matrixDelete", (p[1], "", '.', p[2], p[3], p[4], p[5], p[6], p[7]))

def p_matrixDelete_atIdIndex(p):
    'matrixDelete : ID index DELETE LPARENTHESES INTEGER COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = ASTNode("matrixDelete", (p[1], p[2], '.', p[3], p[4], p[5], p[6], p[7], p[8]))


# Print Statement
def p_printStatement(p):
    'printStatement : PRINT LPARENTHESES printArgument RPARENTHESES SEMICOLON'
    p[0] = ASTNode("printStatement", (p[1], p[2], p[3], p[4], p[5]))

def p_printArgument(p):
    '''printArgument : ID
                    | type
                    | indexedId
                    | len'''
    p[0] = ASTNode("printArgument", [p[1]])


def p_type(p):
    'type : TYPE LPARENTHESES ID RPARENTHESES'
    p[0] = ASTNode("type", (p[1], p[2], p[3], p[4]))


# List Len
def p_len(p):
    'len : LEN LPARENTHESES ID RPARENTHESES'
    p[0] = ASTNode("len", [p[3]])

def p_len_index(p):
    'len : LEN LPARENTHESES ID index RPARENTHESES'
    p[0] = ASTNode("len", [p[3], p[4]])


# Blink
def p_blink_default(p):
    'blink : BLINK LPARENTHESES indexedId COMMA BOOLEAN RPARENTHESES SEMICOLON'
    p[0] = ASTNode("blink", [p[1], p[2], p[3], p[4], p[5], p[6]])

def p_blink_custom(p):
    'blink : BLINK LPARENTHESES indexedId COMMA INTEGER COMMA TIMEUNIT COMMA BOOLEAN RPARENTHESES SEMICOLON'
    p[0] = ASTNode("blink", [p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10]])
