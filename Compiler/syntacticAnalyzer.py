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
#start = 'statementList'

def p_statementList1(p):
    'statementList : statement statementList'
    p[0] = (p[1], p[2])
    #print "statementList1!!!!!!!!!!!!!!"

# def p_statementList2(p):
#     'statementList : statement'
#     p[0] = (p[0], p[1])
#     print "statementList1!!!!!!!!!!!!!!"

def p_statementListEmpty(p):
    'statementList : empty'
    p[0] = p[1]

def p_statement(p):
    'statement : varAssignment'
    p[0] = p[1]
    #print "varAssignment!!!!!!!!!!!!!!"

def p_varAssignment(p):
    'varAssignment : ID ASSIGN expression SEMICOLON'
    p[0] = (p[1], p[2], p[3])#, p[4])

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

def p_empty(p):
	'empty :'
	p[0] = "void"

def p_error(p):
	print "Syntaxis Error "# +str(p.lineno)

data= ''' 
    x = 5;
    y = 3;
    z = 7;
'''

parser = yacc.yacc()
result = parser.parse(data)
print result
