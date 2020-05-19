
import sys
sys.path.append("..")
from DataStructures.ASTNodes import ASTNode


def p_builtInFunction(p):
    'builtInFunction : delay'
    p[0] = ASTNode("builtInFunction", ([p[1]]))


# Delay 
def p_delay_default(p):
    'delay : DELAY LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = ASTNode("delay", (p[1], p[2], p[3], p[4]))

def p_delay_custom(p):
    'delay : DELAY LPARENTHESES INTEGER COMMA TIMEUNIT RPARENTHESES SEMICOLON'
    p[0] = ASTNode("delay", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))


# Default Cube 
def p_defaultCube(p):
    'list : DEFAULTCUBE LPARENTHESES BOOLEAN RPARENTHESES'
    p[0] = ASTNode("defaultCube", (p[1], p[2], p[3], p[4]))