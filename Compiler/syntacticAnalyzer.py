import ply.yacc as yacc

from lexicalAnalyzer import tokens

# Ordered from lowest to highest priority
precedence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
	('left', 'LPARENTHESES', 'RPARENTHESES'),
)

#name of the first production
#start = 'statementList'

def p_statementList_single(p):
    'statementList : statement '
    p[0] = p[1]

def p_statementList_multiple(p):
    'statementList : statement statementList'
    p[0] = (p[1], p[2])
    # avoiding adding a Null nested node 
    # if(p[2] == "empty"):
    #     p[0] = (p[1])
    # else:
    #     p[0] = (p[1], p[2])

def p_statementList_empty(p):
    'statementList : empty'
    p[0] = p[1]

def p_statement(p):
    '''statement : varAssignment 
                 | procedureDeclaration'''
    p[0] = p[1]

def p_varAssignment(p):
    '''varAssignment : simpleAssignment
                     | indexAssignment'''
    p[0] = p[1]

def p_simpleAssignment(p):
    'simpleAssignment : ID ASSIGN varValue SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4])
def p_indexAssignment(p):
    'indexAssignment : ID index ASSIGN varValue SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_index_single(p):
    'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET'
    p[0] = (p[1], p[2], p[3])

def p_index_multiple(p):
    'index : index index'
    p[0] = (p[1], p[2])

# def p_index_1D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[1], p[2], p[3])
# def p_index_2D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
# def p_index_3D(p):
#     'index : LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET LSQUAREBRACKET INTEGER RSQUAREBRACKET'
#     p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_varValue(p):
    '''varValue : numExpression 
                | BOOLEAN
                | list'''
    p[0] = p[1]

# Lists Syntax
def p_list(p):
    'list : LSQUAREBRACKET listElements RSQUAREBRACKET'
    p[0] = (p[1], p[2], p[3])

def p_listElements_single(p):
    'listElements : listElement'
    p[0] = p[1]

def p_listElements_multiple(p):
    'listElements : listElement COMMA listElements'
    p[0] = (p[1], p[2], p[3])

def p_listElements_empty(p):
    'listElements : empty'
    p[0] = p[1]

def p_listElement(p):
    '''listElement : BOOLEAN
                   | list'''
    p[0] = p[1]

# Numerical Operations
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

def p_expression_term(p):
    'numExpression : term'
    p[0] = p[1]

def p_term(p):
    'term : factor'
    p[0] = p[1]

def p_factor(p):
    'factor : INTEGER'
    p[0] = p[1]

# Procedures Syntax
def p_procedureDeclaration(p):
    'procedureDeclaration : PROCEDURE ID LPARENTHESES parameters RPARENTHESES LBRACE statementList RBRACE SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_parameters_single(p):
    'parameters : parameter'
    p[0] = p[1]

def p_parameters_multiple(p):
    'parameters : parameter COMMA parameters '
    p[0] = (p[1], p[2], p[3])

def p_parameter(p):
    'parameter : ID'
    p[0] = p[1]

def p_parameters_empty(p):
    'parameters : empty'
    p[0] = p[1]

def p_empty(p):
	'empty :'
	p[0] = None

def p_error(p):
	print "Syntaxis Error "# +str(p.lineno)

data= ''' 
    procedure sum(a,b){
        x = 5;
        y = 10;
    };
    list = [true, false];
'''

# to supress unused tokens warnings
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)

parser = yacc.yacc()
result = parser.parse(data)
print result
