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
        anotherList = [true, true];
        
        anotherList.insert(0, false);
        Cubo.insert(false, 0, 0);
        
        anotherList.del(0);
        Cubo.del(0, 1);
        
        if false == false {
            Delay();
        };
        
        for row in Cubo Step 2{
            Delay();
        };
    };
'''

compile(code)
