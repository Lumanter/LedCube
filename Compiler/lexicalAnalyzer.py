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
    'if': 'IF',
	'else': 'ELSE',
	'for': 'FOR'
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

	# Logical Comparators
	'EQUALS',
	'LESSTHAN',
	'GREATERTHAN',

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

tokens = tokens + list(keywords.values())



