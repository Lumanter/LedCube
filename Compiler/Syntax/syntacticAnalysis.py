import ply.yacc as yacc
import sys
sys.path.append("..")

from Lexic.lexicAnalysis import  tokens
from DataStructures.ASTNodes import *
from numericalOperations import *
from configurationConstants import *
from variableAssignments import *
from statements import *
from builtinFunctions import *
from lists import *
from procedures import *

start = 'program'

def p_program(p):
    'program : configurationConstants statementList'
    p[0] = program("program", (p[1], p[2]))

def p_error(p):
    if(p == None):
        print "Syntax error at the last character"
    else:
        print "Syntaxis error in line " + str(p.lineno) + ", immediately before character \""+str(p.value)+"\""

syntacticAnalyzer = yacc.yacc()

# supress unused tokens warnings 
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)
