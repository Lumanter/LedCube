
# Statements
def p_statementList_one(p):
    'statementList : statement '
    p[0] = p[1]

def p_statementList_many(p):
    'statementList : statement statementList'
    p[0] = (p[1], p[2])

def p_statementList_empty(p):
    'statementList : empty'
    p[0] = p[1]

def p_statement(p):
    '''statement : varAssignment 
                 | procedureDeclaration
                 | procedureCall
                 | builtInFunction
                 | ifStatement
                 | forLoop
                 | listDelete
                 | listInsert'''
    p[0] = p[1]

def p_empty(p):
	'empty :'
	p[0] = None