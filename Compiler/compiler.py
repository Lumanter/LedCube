from Syntax.syntacticAnalysis import syntacticAnalyzer
from ErrorHandling.ErrorHandler import *
from CodeProduction.codeGenerator import getFinalCode

from Semantic.Utils import *

def compile(code):

    areNotLexicErrors = (syntacticAnalyzer != None)
    if areNotLexicErrors:
        ast = syntacticAnalyzer.parse(code)

        areNotSyntaxErrors = (ast != None)
        if areNotSyntaxErrors:
            ast.translation()

            producedCode = getFinalCode()

            print "Final Code:"
            print producedCode

        else:
            print "AST couldn't be build due to syntax error"
    else:
        print "AST couldn't be build due to lexic error"
