import ply.lex as lex
import sys
sys.path.append("..")
from Compiler.ErrorHandling.ErrorHandler import *

keywords = {

    # Configuration Constants
    'Delay': 'DELAY',
    'Timer': 'TIMER',
    'Rango_timer': 'RANGO_TIMER',
    'Dim_filas': 'DIM_FILAS',
    'Dim_columnas': 'DIM_COLUMNAS',
    'Cubo': 'CUBO',

    # Procedure
    'Procedure': 'PROCEDURE',
    'CALL': 'CALL',

    # Built-in Functions
    'defaultCube': 'DEFAULTCUBE',
    'list': 'LIST',
	'range': 'RANGE',
    'print': 'PRINT',

    # Control Flow
    'if': 'IF',
	'for': 'FOR',
	'in': 'IN',
	'Step': 'STEP'

}

tokens = [
    'ID',
    'ASSIGN',

    # Variable Types
    'INTEGER',
    'BOOLEAN',
    'TIMEUNIT',

    # List Functions
	'LISTOPERATOR',
    'LISTDIMENSION',
    'DELETE',
	'INSERT',

    # Logical Operator
	'COMPARATOR',

    # Numerical Operators
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'POWER',
    'MODULO',

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
t_ignore = ' \t\r'  # ignore spaces, tabs and windows' carry
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
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_LISTOPERATOR(t):
	r'\.(F|T|Neg)'
	t.value = t.value[1:]
	return t

def t_LISTDIMENSION(t):
	r'\.shape(A|F|C)'
	t.value = t.value[1:]
	return t

def t_DELETE(t):
	r'\.del'
	t.value = t.value[1:]
	return t

def t_INSERT(t):
	r'\.insert'
	t.value = t.value[1:]
	return t

def t_COMPARATOR(t):
	r'>=|<=|>|<|==|!='
	return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9@_&]*'
    if t.value in keywords:
        if t.value != "Cubo":
            t.value = t.value.upper()
            t.type = t.value
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
    logError("Lexical error: Illegal character '" + t.value[0] + "' at line number " + str(t.lexer.lineno))
    t.lexer.skip(1)

lexicalAnalyzer = lex.lex()
