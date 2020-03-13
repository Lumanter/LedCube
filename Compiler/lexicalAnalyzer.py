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
t_ignore = '\t ' #ignore spaces and tabs
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\*\*'
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
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in keywords:
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_INTEGER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_BOOLEAN(t):
	r'true|false'
	t.value = (t.value == 'true')
	return t