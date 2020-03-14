import ply.yacc as yacc

from lexicalAnalyzer import tokens

# Ordered from lowest to highest priority
precedence = (
    #('nonassoc', 'LESSTHAN', 'GREATERTHAN'),
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
	('left', 'LPARENTHESES', 'RPARENTHESES'),
)

#name of the first production
#start = 'program'

# def p_varDeclares1(p):
#     'program : varDeclare '
#     p[0] = p[1]

# def p_varDeclares1(p):
#     'program : varDeclares varDeclare'
#     p[0] = str(p[1]) + str(p[2])

def p_varDeclare(p):
    'var : ID ASSIGN expression SEMICOLON'
    p[0] = p[1] + " = " + str(p[3]) + p[4]

# Numerical Operations
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_uminus(p):
    'expression : MINUS term'
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

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_integer(p):
    'factor : INTEGER'
    p[0] = p[1]

# def p_empty(p):
# 	'empty :'
# 	pass

def p_error(p):
	print "Syntaxis Error at line " +str(p.lineno)

data= ''' 
    x = -11 - 3 + 4 ** 2 /2;
'''

parser = yacc.yacc()
result = parser.parse(data)
print result