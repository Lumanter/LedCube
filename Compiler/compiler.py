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


code = '''
    Timer = 500;
    Rango_timer = "Mil";
    Dim_filas = 8;
    Dim_columnas = 8;
    Cubo = defaultCube(false);
    
    Procedure Main() {
        for x in 8{
            for y in 8{
                for z in 8{
                    Cubo[x][y][z] = true;
                };
            };
        };
    };
'''


compile(code)
