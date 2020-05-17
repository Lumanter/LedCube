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
        Delay();
    };
'''

compile(code)