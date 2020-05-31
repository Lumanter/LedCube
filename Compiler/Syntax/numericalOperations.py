import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode

# Ordered from lowest to highest priority
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
    ('left', 'LPARENTHESES', 'RPARENTHESES'),
)

def p_numExpression_1(p):
    'numExpression : LPARENTHESES numExpression RPARENTHESES'
    p[0] = ASTNode("numExpression", (p[1], p[2], p[3]))

def p_numExpression_2(p):
    'numExpression : numExpression numOperator numExpression'
    p[0] = ASTNode("numExpression", (p[1], p[2], p[3]))

def p_numExpression_3(p):
    'numExpression : numExpression numOperator numValue'
    p[0] = ASTNode("numExpression", (p[1], p[2], p[3]))

def p_numExpression_4(p):
    'numExpression : numValue numOperator numExpression'
    p[0] = ASTNode("numExpression", (p[1], p[2], p[3]))

def p_numExpression_5(p):
    'numExpression : numValue numOperator numValue'
    p[0] = ASTNode("numExpression", (p[1], p[2], p[3]))

def p_numOperator(p):
    '''numOperator : PLUS
                   | MINUS
                   | MULTIPLY
                   | DIVIDE
                   | POWER
                   | MODULO'''
    p[0] = p[1]

def p_numValue(p):
    '''numValue : ID
                | INTEGER'''
    p[0] = ASTNode("numValue", [p[1]])