from Syntax.syntacticAnalysis import syntacticAnalyzer

def compile(code):
    ast = syntacticAnalyzer.parse(code)
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
        y = 0;
        z = 0;
        lista1D = [true,true,true,true];
        lista2D = [[true,true],[true,true]];
        lista3D = [[[true,true],[true,true]],[[true,true],[true,true]],[[true,true],[true,true]]];
        CALL turnOn(0,0,1);
        CALL turnOn(0,1,1);
    };
'''

compile(code)