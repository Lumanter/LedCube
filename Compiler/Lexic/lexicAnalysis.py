import ply.lex as lex
import sys
sys.path.append("..")
from Compiler.ErrorHandling.ErrorHandler import *

from tokens import *

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
t_COLON = r':'


# Regular expressions for not so simple tokens
def t_TIMEUNIT(t):
    r'\"(Mil|Seg|Min|Nada)\"'
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

# Necessary due to ID's first letter lowercase restriction
def t_keywords(t):
    r'Rango_timer|Dim_columnas|defaultCube|Timer|Dim_filas|Procedure|CALL|Step|Delay|Blink'
    t.value = t.value.upper()
    t.type = t.value
    return t

# Only ones treated as ID's with first lowercase
def t_IDExceptions(t):
    r'Cubo|Main'
    t.type = "ID"
    return t

def t_ID(t):
    r'([a-z]{1})([a-zA-Z0-9@_&]{0,9})'
    if t.value in keywords:
        if t.value != "Cubo":
            t.value = t.value.upper()
            t.type = t.value
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
	r'--.*'
	pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    logError("Lexical error: Illegal character '" + t.value[0] + "' at line number " + str(t.lexer.lineno))
    t.lexer.skip(1)

def t_eof(t):
    t.lexer.lineno = 1

lexicalAnalyzer = lex.lex()

def lexicAnalysis(code):
    lexicalAnalyzer.input(code)
    tokenLeft = True
    while tokenLeft:
        tokenLeft = lexicalAnalyzer.token()
        # if tokenLeft:
        #     print str(tokenLeft.type) + ": " + str(tokenLeft.value)
