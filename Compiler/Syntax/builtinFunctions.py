
import sys
sys.path.append("..")
from DataStructures.ASTNodes import ASTNode


def p_builtInFunction(p):
    '''builtInFunction : delay
                       | listOperation'''
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