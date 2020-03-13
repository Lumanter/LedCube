import ply.lex as lex
# imports for testing purposes
import re
import codecs
import os
import sys

keywords = {
	'main': 'MAIN',
    'procedure': 'PROCEDURE',
    'call': 'CALL',
	#'if': 'IF',
	#'else': 'ELSE',
	#'for': 'FOR'
	'delay': 'DELAY'
}

tokens = [
	'ID',
	'ASSIGN',

	# Variable Types
	'INTEGER',
	'BOOLEAN',

	# open to discussion
	'TIMEUNIT',

	# Numerical Operators 
	'PLUS',
	'MINUS',
	'MULTIPLY',
	'DIVIDE',
	'POWER',
	'MODULO',

	# Logical Comparators
	#'EQUALS',
	#'LESSTHAN',
	#'GREATERTHAN',

	# Enclosing Characters
	'LPARENTHESES', 
	'RPARENTHESES',
	'LSQUAREBRACKET', 
	'RSQUAREBRACKET',
	'LBRACE', 
	'RBRACE',
	
	# Punctuation Marks
	'COMMA',
	'SEMMICOLON',
	'DOT'
	]

# Adding the keywords to the total tokens
tokens = tokens + list(keywords.values())

# Regular expressions for simple tokens
t_POWER = r'\*\*'
t_ignore = ' \t\r' #ignore spaces and tabs
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
t_SEMMICOLON = r';'
t_DOT = r'\.'

# Regular expressions for not so simple tokens
def t_TIMEUNIT(t):
	r'\"(Mil|Seg|Min)\"'
	t.value = t.value[1:-1]
	return t

def t_BOOLEAN(t):
	r'true|false'
	t.value = (t.value == 'true')
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9@_&]*'
	if t.value.lower() in keywords:
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
	print "Lexical error: Illegal character '" + t.value[0] + "' at line number " + str(t.lexer.lineno)
	t.lexer.skip(1)

lexicalAnalyzer = lex.lex()

# Tester
# data = '''
# 	Timer = 1;
# 	Rango_timer = \"Seg\";
# 	Dim_Filas = 8;
# 	Dim_Columnas = 8;
# 	Cubo = [];

# 	Procedure turnOnLed(x, y, z) {
# 		Cubo[x][y][z] = true;	
# 	}
# '''

# '''
# 	Procedure Main() {
# 		myBoolean = true;
# 		x = 6 / 2 + 3 ** 8 - 1;
# 		y = 10 % 2;
# 		call turnOnLed(0, 0, 0);
# 		Delay() 
# 	}
# '''
# lexicalAnalayzer.input(data)
# for token in lexicalAnalayzer:
#     print(token.type, token.value)