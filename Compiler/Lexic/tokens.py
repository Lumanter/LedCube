
keywords = {

    # Configuration Constants
    'Delay': 'DELAY',
    'Timer': 'TIMER',
    'Dim_filas': 'DIM_FILAS',
    'Cubo': 'CUBO',

    # Procedure
    'Procedure': 'PROCEDURE',
    'CALL': 'CALL',

    # Built-in Functions
    'list': 'LIST',
	'range': 'RANGE',
    'print': 'PRINT',
    'type': 'TYPE',
    'len': 'LEN',

    # Control Flow
    'if': 'IF',
	'for': 'FOR',
	'in': 'IN',
	'Step': 'STEP'

}

tokens = [

    'ID',

    # Id max 10 length exceptions
    'RANGO_TIMER',
    'DIM_COLUMNAS',
    'DEFAULTCUBE',

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
    'SEMICOLON',
    'COLON',

    # Misc
    'COMMENT'
]

# Adding the keywords to the total tokens
tokens = tokens + list(keywords.values())