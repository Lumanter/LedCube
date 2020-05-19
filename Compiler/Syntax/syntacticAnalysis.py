import ply.yacc as yacc
import sys
sys.path.append("..")
from ErrorHandling.ErrorHandler import *

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
    errorMessage = "Syntax error at the last character"
    if (p != None):
        errorMessage = logError("Syntaxis error in line " + str(p.lineno) + ", immediately before character \""+str(p.value)+"\"")
    print errorMessage
    logError(errorMessage)


resetErrorLog()
syntacticAnalyzer = None
if not areCompileErrors():
    syntacticAnalyzer = yacc.yacc()

# supress unused tokens warnings
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)
