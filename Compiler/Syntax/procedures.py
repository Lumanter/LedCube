
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode

# Procedure Declaration 
def p_procedureDeclaration_noParameters(p):
    'procedureDeclaration : PROCEDURE ID LPARENTHESES RPARENTHESES LBRACE statementList RBRACE SEMICOLON'
    p[0] = ASTNode("procedureDeclaration", (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))


def p_procedureDeclaration_parameters(p):
    'procedureDeclaration : PROCEDURE ID LPARENTHESES parameters RPARENTHESES LBRACE statementList RBRACE SEMICOLON'
    p[0] = ASTNode("procedureDeclaration", (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))


def p_parameters_one(p):
    'parameters : parameter'
    p[0] = ASTNode("parameters", [p[1]])


def p_parameters_many(p):
    'parameters : parameter COMMA parameters '
    p[0] = ASTNode("parameters", (p[1], p[2], p[3]))


def p_parameter(p):
    'parameter : ID'
    p[0] = ASTNode("parameter", [p[1]])


# Procedure Call 
def p_procedureCall_noParameters(p):
    'procedureCall : CALL ID LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = ASTNode("procedureCall", (p[1], p[2], p[3], p[4], p[5]))


def p_procedureCall_parameters(p):
    'procedureCall : CALL ID LPARENTHESES arguments RPARENTHESES SEMICOLON'
    p[0] = ASTNode("procedureCall", (p[1], p[2], p[3], p[4], p[5], p[6]))


def p_arguments_one(p):
    'arguments : argument'
    p[0] = ASTNode("arguments", [p[1]])


def p_arguments_many(p):
    'arguments : argument COMMA arguments'
    p[0] = ASTNode("arguments", (p[1], p[2], p[3]))


def p_argument(p):
    'argument : varValue'
    p[0] = ASTNode("argument", [p[1]])

