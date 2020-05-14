import ply.yacc as yacc
from lexicalAnalysis import tokens
from semanticAnalysis import *
from Utils import findNumValue

# Ordered from lowest to highest priority
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
    ('left', 'LPARENTHESES', 'RPARENTHESES'),
)


# name of the first production
# start = 'statementList'

def p_program(p):
    'program : configurationConstants statementList'
    p[0] = program("program", (p[1], p[2]))


# TEMPORTAL FOR TESTING REASONS
# def p_configurationConstants_empty(p):
#     'configurationConstants : empty'
#     p[0] = p[1]

# Configuration Constants
def p_configurationConstants(p):
    'configurationConstants : timer timeUnit rows columns cube'
    p[0] = configurationConstants("configurationConstants", (p[1], p[2], p[3], p[4], p[5]))


def p_timer(p):
    'timer : TIMER ASSIGN INTEGER SEMICOLON'
    p[0] = timer("timer", (p[1], p[2], p[3], p[4]))


def p_timeUnit(p):
    'timeUnit : RANGO_TIMER ASSIGN TIMEUNIT SEMICOLON'
    p[0] = timeUnit("timeUnit", (p[1], p[2], p[3], p[4]))


def p_rows(p):
    'rows : DIM_FILAS ASSIGN INTEGER SEMICOLON'
    p[0] = rows("rows", (p[1], p[2], p[3], p[4]))


def p_columns(p):
    'columns : DIM_COLUMNAS ASSIGN INTEGER SEMICOLON'
    p[0] = columns("columns", (p[1], p[2], p[3], p[4]))


def p_cube(p):
    'cube : ID ASSIGN list SEMICOLON'
    p[0] = cube("cube", (p[1], p[2], p[3], p[4]))


# Statement Productions
def p_statementList_one(p):
    'statementList : statement '
    p[0] = statementList_one("statementList", [p[1]])


def p_statementList_many(p):
    'statementList : statement statementList'
    p[0] = statementList_many("statementList", (p[1], p[2]))


def p_statementList_empty(p):
    'statementList : empty'
    p[0] = statementList_empty("statementList", [p[1]])


def p_statement(p):
    '''statement : varAssignment 
                 | procedureDeclaration
                 | procedureCall
                 | builtInFunction'''
    p[0] = statement("statement", [p[1]])


# Variable Assignment Productions
def p_varAssignment(p):
    '''varAssignment : simpleAssignment
                     | indexAssignment'''
    p[0] = varAssignment("varAssignment", [p[1]])


def p_simpleAssignment(p):
    'simpleAssignment : ID ASSIGN varValue SEMICOLON'
    p[0] = simpleAssignment("simpleAssignment", (p[1], p[2], p[3], p[4]))


def p_indexAssignment(p):
    'indexAssignment : ID index ASSIGN varValue SEMICOLON'
    p[0] = indexAssignment("indexAssignment", (p[1], p[2], p[3], p[4], p[5]))


def p_index_one(p):
    'index : LSQUAREBRACKET indexValue RSQUAREBRACKET'
    p[0] = index_one("index", (p[1], p[2], p[3]))


def p_index_many(p):
    'index : index index'
    p[0] = index_many("index", (p[1], p[2]))


def p_indexValue(p):
    '''indexValue : INTEGER 
                  | ID'''
    p[0] = indexValue("indexValue", ([p[1]]))


# productions to restrain index to 3 indexes
# def p_index_1D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[0], p[1], p[2], p[3])
# def p_index_2D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[0], p[1], p[2], p[3], p[4], p[5], p[6])
# def p_index_3D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_varValue(p):
    '''varValue : ID
                | numExpression 
                | BOOLEAN
                | list'''
    p[0] = varValue("varValue", ([p[1]]))


# Built In Functions Syntax Productions
def p_builtInFunction(p):
    'builtInFunction : delay'
    p[0] = builtInFunction("builtInFunction", ([p[1]]))

    # Delay Productions


def p_delay_default(p):
    'delay : DELAY LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = delay_default("delay", (p[1], p[2], p[3], p[4]))


def p_delay_custom(p):
    'delay : DELAY LPARENTHESES INTEGER COMMA TIMEUNIT RPARENTHESES SEMICOLON'
    p[0] = delay_custom("delay", (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))


# Lists Syntax Productions
def p_list_empty(p):
    'list : LSQUAREBRACKET RSQUAREBRACKET'
    p[0] = list_empty("list", (p[1], p[2]))


def p_list(p):
    'list : LSQUAREBRACKET listElements RSQUAREBRACKET'
    p[0] = list("list", (p[1], p[2], p[3]))


def p_listElements_one(p):
    'listElements : listElement'
    p[0] = listElements_one("listElements", ([p[1]]))


def p_listElements_many(p):
    'listElements : listElement COMMA listElements'
    p[0] = listElements_many("listElements", (p[1], p[2], p[3]))


def p_listElement(p):
    '''listElement : BOOLEAN
                   | list'''
    p[0] = listElement("listElement", ([p[1]]))


# Numerical Operations Productions
# don't support ids yet
# they return the number itself so the tupple (aka tree) isn't propagated
def p_numExpression_plus(p):
    'numExpression : numExpression PLUS term'
    p[0] = p[1] + p[3]

def p_numExpression_minus(p):
    'numExpression : numExpression MINUS term'
    p[0] = p[1] - p[3]

def p_numExpression_uminus(p):
    'numExpression : MINUS term'
    p[0] = - p[2]

def p_term_multiply(p):
    'term : term MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    'term : term MODULO factor'
    p[0] = p[1] % p[3]

def p_term_power(p):
    'term : term POWER factor'
    p[0] = p[1] ** p[3]

def p_numExpression_term(p):
    'numExpression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_integer(p):
    'factor : INTEGER'
    p[0] = p[1]


# Procedure Declaration Syntax
def p_procedureDeclaration_noParameters(p):
    'procedureDeclaration : PROCEDURE ID LPARENTHESES RPARENTHESES LBRACE statementList RBRACE SEMICOLON'
    p[0] = procedureDeclaration_noParameters("procedureDeclaration", (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))


def p_procedureDeclaration_parameters(p):
    'procedureDeclaration : PROCEDURE ID LPARENTHESES parameters RPARENTHESES LBRACE statementList RBRACE SEMICOLON'
    p[0] = procedureDeclaration_parameters("procedureDeclaration",
                                           (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))


def p_parameters_one(p):
    'parameters : parameter'
    p[0] = parameters_one("parameters", [p[1]])


def p_parameters_many(p):
    'parameters : parameter COMMA parameters '
    p[0] = parameters_many("parameters", (p[1], p[2], p[3]))


def p_parameter(p):
    'parameter : ID'
    p[0] = parameter("parameter", [p[1]])


# Procedure Call Syntax Productions
def p_procedureCall_noParameters(p):
    'procedureCall : CALL ID LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = procedureCall_noParameters("procedureCall", (p[1], p[2], p[3], p[4], p[5]))


def p_procedureCall_parameters(p):
    'procedureCall : CALL ID LPARENTHESES arguments RPARENTHESES SEMICOLON'
    p[0] = procedureCall_parameters("procedureCall", (p[1], p[2], p[3], p[4], p[5], p[6]))


def p_arguments_one(p):
    'arguments : argument'
    p[0] = arguments_one("arguments", [p[1]])


def p_arguments_many(p):
    'arguments : argument COMMA arguments'
    p[0] = arguments_many("arguments", (p[1], p[2], p[3]))


def p_argument(p):
    'argument : varValue'
    p[0] = argument("argument", [p[1]])


# Special productions
def p_empty(p):
    'empty :'
    p[0] = None


def p_error(p):
    print "Syntaxis Error at character " + str(p.value) + ", in line " + str(p.lineno)


syntacticAnalyzer = yacc.yacc()

# extra stuff for temporal tests
data = '''
    Timer = 500;
    Rango_timer = "Mil";
    Dim_filas = 8;
    Dim_columnas = 8;
    Cubo = [];

    Procedure sum(a,b) {
        x = 5;
        z = True;
        y = 25;
        Delay();
        Delay();
        Delay();
        Delay();
    };
    list = [true, false];
    y = 7;

    Procedure Main() {
        x[0][0][0] = true;
        CALL sum(5,5);
    };
'''

# supressing unused tokens warnings for cleaner console logging
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)

result = syntacticAnalyzer.parse(data)
print result
