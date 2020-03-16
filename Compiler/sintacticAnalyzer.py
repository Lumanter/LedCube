import ply.yacc as yacc

from lexicalAnalyzer import tokens

# Ordered from lowest to highest priority
precedence = (
    #('nonassoc', 'LESSTHAN', 'GREATERTHAN'),
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
	('left', 'LPARENTHESES', 'RPARENTHESES'),
    ('right', 'ID'),
    ('right', 'ASSIGN')
)

#def p_program(p):
#    '''program : constDeclares statementList main'''
#    p[0] = p[1] + p[2] + p[3]

def p_constDeclares(p):
    '''constDeclares : timerDeclare timerUnitDeclare rowsDeclare columnsDeclare cubeDeclare'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_timerDeclare(p):
    '''timerDeclare : TIMER ASSIGN INTEGER SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

def p_timerUnitDeclare(p):
    '''timerUnitDeclare : RANGO_TIMER ASSIGN TIMEUNIT SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

def p_rowsDeclare(p):
    '''rowsDeclare : DIM_FILAS ASSIGN INTEGER SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

def p_columnsDeclare(p):
    '''columnsDeclare : DIM_COLUMNAS ASSIGN INTEGER SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

def p_cubeDeclare(p):
    #temporally is going to be a INTEGER but should be change to a list in the future
    '''cubeDeclare : CUBO ASSIGN INTEGER SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

#name of the first production
#start = 'program'

#def p_varDeclares1(p):
 #   'program : varDeclare '
  #  p[0] = p[1]

# def p_varDeclares1(p):
#     'program : varDeclares varDeclare'
#     p[0] = str(p[1]) + str(p[2])

def p_varDeclare(p):
    '''var : ID ASSIGN expression SEMICOLON'''
    p[0] = p[1] + " = " + str(p[3]) + p[4]

# Numerical Operations
def p_expression_plus(p):
    '''expression : expression PLUS term'''
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    '''expression : expression MINUS term'''
    p[0] = p[1] - p[3]

def p_expression_uminus(p):
    '''expression : MINUS term'''
    p[0] = - p[2]

def p_term_multiply(p):
    '''term : term MULTIPLY factor'''
    p[0] = p[1] * p[3]

def p_term_divide(p):
    '''term : term DIVIDE factor'''
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    '''term : term MODULO factor'''
    p[0] = p[1] % p[3]

def p_term_power(p):
    '''term : term POWER factor'''
    p[0] = p[1] ** p[3]

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_integer(p):
    '''factor : INTEGER'''
    p[0] = p[1]

# def p_empty(p):
# 	'empty :'
# 	pass

def p_error(p):
	print "Syntaxis Error at line " + str(p.lineno)

data= ''' 
    x = -11 - 3 + 4 ** 2 /2;
'''

parser = yacc.yacc()
result = parser.parse(data)
print result