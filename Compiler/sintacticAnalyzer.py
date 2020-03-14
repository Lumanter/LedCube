import ply.yacc as yacc

from lexicalAnalyzer import tokens

# Ordered from lowest to highest priority
precedence = (
	('right','ID', 'CALL'),
	('right', 'PROCEDURE'),
	('right', 'ASSIGN'),
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
	('left', 'LPARENT', 'RPARENT'),
)
