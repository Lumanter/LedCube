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

# extra stuff for temporal tests
data= '''
    Timer = 500;
    Rango_timer = "Mil";
    Dim_filas = 8;
    Dim_columnas = 8;
    Cubo = [];

    rows = Cubo.shapeF;
'''

'''
    Procedure sum(a,b) {
        x = 5 + 7 * 9;
        Delay(5,"Mil");
    };
    list = [true, false];
    CALL sum(5,5);
    y = 7;

    Procedure main() {
        x[0][0][0] = true; 
    };
'''
syntacticAnalyzer = yacc.yacc()
print syntacticAnalyzer.parse(data)
