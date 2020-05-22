import ply.yacc as yacc
import sys
import warnings
sys.path.append("..")

from Compiler.ErrorHandling.ErrorHandler import *
from Compiler.Lexic.lexicAnalysis import  tokens
from Compiler.DataStructures.ASTNodes import *
from numericalOperations import *
from configurationConstants import *
from variableAssignments import *
from statements import *
from builtinFunctions import *
from lists import *
from procedures import *
from flowControl import  *

start = 'program'

def p_program(p):
    'program : configurationConstants statementList'
    p[0] = program("program", (p[1], p[2]))

def p_error(p):
    errorMessage = "Syntax error at the last character"
    if (p != None):
        errorMessage = "Syntaxis error in line " + str(p.lineno) + ", immediately before character \""+str(p.value)+"\""
    logError(errorMessage)


syntacticAnalyzer = yacc.yacc()

# supress unused tokens warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)
