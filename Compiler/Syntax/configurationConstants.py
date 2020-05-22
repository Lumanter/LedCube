
import sys
sys.path.append("..")
from Compiler.DataStructures.ASTNodes import ASTNode


def p_configurationConstants(p):
    'configurationConstants : timer timeUnit rows columns cube'
    p[0] = ASTNode("configurationConstants", (p[1], p[2], p[3], p[4], p[5]))


def p_timer(p):
    'timer : TIMER ASSIGN INTEGER SEMICOLON'
    p[0] = ASTNode("timer", (p[1], p[2], p[3], p[4]))


def p_timeUnit(p):
    'timeUnit : RANGO_TIMER ASSIGN TIMEUNIT SEMICOLON'
    p[0] = ASTNode("timeUnit", (p[1], p[2], p[3], p[4]))


def p_rows(p):
    'rows : DIM_FILAS ASSIGN INTEGER SEMICOLON'
    p[0] = ASTNode("rows", (p[1], p[2], p[3], p[4]))


def p_columns(p):
    'columns : DIM_COLUMNAS ASSIGN INTEGER SEMICOLON'
    p[0] = ASTNode("columns", (p[1], p[2], p[3], p[4]))


def p_cube(p):
    'cube : ID ASSIGN list SEMICOLON'
    p[0] = ASTNode("cube", (p[1], p[2], p[3], p[4]))