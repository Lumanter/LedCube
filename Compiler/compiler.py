from Syntax.syntacticAnalysis import syntacticAnalyzer
from ErrorHandling.ErrorHandler import *

def compile(code):
    areNotLexicErrors = (syntacticAnalyzer != None)
    if areNotLexicErrors:
        ast = syntacticAnalyzer.parse(code)
        areNotSyntaxErrors = (ast != None)
        if areNotSyntaxErrors:
            ast.translation()
        else:
            print "ast could not be build due to syntax error"
    else:
        print "ast could not be build due to lexic error"
    # targetCode = generateTargetCode(ast)
    # return targetCode 

code = '''
    Timer = 500;
    Rango_timer = "Mil";
    Dim_filas = 8;
    Dim_columnas = 8;
    Cubo = defaultCube(false);

    Procedure turnOn(x, y, z) {
        Cubo[x][y][z] = true;
    };

    Procedure Main() {
        x = 0;
        y = 1;
        z = 2;
        lista1D = [true,true,true,true];
        lista2D = [[true,true],[true,true]];
        lista3D = [[[true,true],[true,true]],[[true,true],[true,true]],[[true,true],[true,true]]];
        lista1D[x] = false;
        lista2D[x][y] = false;
        lista3D[x][y][y] = false;
        CALL turnOn(0,0,1);
        CALL turnOn(0,1,1);
    };
'''

compile(code)
