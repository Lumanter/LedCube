import ply.lex as lex

keywords = {
    'Procedure': 'PROCEDURE',
    'CALL': 'CALL',

	# Configuration Constants
	'Timer': 'TIMER',
	'Rango_timer': 'RANGO_TIMER',
	'Dim_filas': 'DIM_FILAS',
	'Dim_columnas': 'DIM_COLUMNAS',
	'Cubo': 'CUBO',

	'if': 'IF',
	'for': 'FOR',
	'in': 'IN',
	'Step': 'STEP',
	'Delay': 'DELAY'
}

tokens = [
	'ID',
	'ASSIGN',

	# Variable Types
	'INTEGER',
	'BOOLEAN',
	'TIMEUNIT',

	# List Functions
	'LISTDIMENSION',
	'LISTOPERATOR',

	# Numerical Operators 
	'PLUS',
	'MINUS',
	'MULTIPLY',
	'DIVIDE',
	'POWER',
	'MODULO',

	# Logical Operator 
	'COMPARATOR',

	# Enclosing Characters
	'LPARENTHESES', 
	'RPARENTHESES',
	'LSQUAREBRACKET', 
	'RSQUAREBRACKET',
	'LBRACE', 
	'RBRACE',
	
	# Punctuation Marks
	'COMMA',
	'SEMICOLON'
]

# Adding the keywords to the total tokens
tokens = tokens + list(keywords.values())

# Regular expressions for simple tokens
t_POWER = r'\*\*'
t_ignore = ' \t\r' #ignore spaces, tabs and windows' carry 
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'\%'
t_LPARENTHESES = r'\(' 
t_RPARENTHESES = r'\)' 
t_LSQUAREBRACKET = r'\[' 
t_RSQUAREBRACKET = r'\]' 
t_LBRACE = r'\{' 
t_RBRACE = r'\}' 
t_COMMA = r','
t_SEMICOLON = r';'

# Regular expressions for not so simple tokens
def t_TIMEUNIT(t):
	r'\"(Mil|Seg|Min)\"'
	t.value = t.value[1:-1]
	return t

	
def t_BOOLEAN(t):
	r'True|False'
	t.value = (t.value == 'True')
	return t

def t_LISTOPERATOR(t):
	r'\.(F|T|Neg)'
	t.value = t.value[1:]
	return t

def t_LISTDIMENSION(t):
	r'\.shape(A|F|C)'
	t.value = t.value[1:]
	return t

def t_COMPARATOR(t):
	r'>=|<=|>|<|==|!='
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9@_&]*'
	if t.value in keywords:
		if t.value != "Cubo":
			t.type = t.value.upper()
	#print t.value, t.type
	return t

def t_INTEGER(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Tracking the line number, for error messaging 
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print "Lexical error: Illegal character '" + t.value[0] + "' at line number " + str(t.lexer.lineno)
	t.lexer.skip(1)

lexicalAnalyzer = lex.lex()
