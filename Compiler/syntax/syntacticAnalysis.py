import ply.yacc as yacc

import sys
sys.path.append('../')
from lexicalAnalysis import tokens

from numericalOperations import *
from configurationConstants import *
from variableAssignments import *
from builtinFunctions import *
from lists import *
from procedures import *
from statements import *

start = 'program'

def p_program(p):
    'program : configurationConstants statementList'
    p[0] = (p[1], p[2])

def p_error(p):
	print "Syntaxis error in line " + str(p.lineno) + ", immediately before character \""+str(p.value)+"\""

syntacticAnalyzer = yacc.yacc()

# extra stuff for temporal tests
data= '''
    Timer = 500;
    Rango_timer = "Mil";
    Dim_filas = 8;
    Dim_columnas = 8;
    Cubo = [];

    rows = Cubo.shapeF;
    x[0][1][8].Neg;
    y[4].T;
    x[8][2][0].F;
'''

program = syntacticAnalyzer.parse(data)

def printTuple(myTuple):
    for subTuple in myTuple:
        if isinstance(subTuple[0], tuple):
            printTuple(subTuple)
        else:
            print subTuple

# print "\n" + "Syntax Analysis Result:" + "\n"
# printTuple(program[1])