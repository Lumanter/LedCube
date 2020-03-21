
# Variable Assignments
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

def p_index_one(p):
    'index : LSQUAREBRACKET indexValue RSQUAREBRACKET'
    p[0] = (p[1], p[2], p[3])

def p_index_many(p):
    'index : index index'
    p[0] = (p[1], p[2])

def p_indexValue(p):
    '''indexValue : INTEGER 
                  | ID'''
    p[0] = p[1]

# productions to restrain index to 3 indexes
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
    '''varValue : ID
                | numExpression 
                | BOOLEAN
                | list'''
    p[0] = p[1]