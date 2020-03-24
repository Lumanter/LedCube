
# Variable Assignments
def p_varAssignment(p):
    '''varAssignment : simpleAssignment
                     | indexAssignment
                     | multipleAssignment'''
    p[0] = p[1]

def p_simpleAssignment(p):
    'simpleAssignment : ID ASSIGN varValue SEMICOLON'
    p[0] = (p[1], p[2], p[3])

def p_indexAssignment(p):
    'indexAssignment : indexedId ASSIGN varValue SEMICOLON'
    p[0] = (p[1], p[2], p[3])

def p_indexedId(p):
    'indexedId : ID index'
    p[0] = (p[1], p[2])

def p_index_one(p):
    'index : LSQUAREBRACKET indexValue RSQUAREBRACKET'
    p[0] = (p[1], p[2], p[3])

def p_index_many(p):
    'index : index index'
    p[0] = (p[1], p[2])

def p_indexValue(p):
    '''indexValue : INTEGER 
                  | ID
                  | indexRange'''
    p[0] = p[1]

def p_indexRange(p):
    'indexRange : INTEGER COLON INTEGER'
    p[0] = (p[1], p[2], p[3])

def p_indexRange_fromStart(p):
    'indexRange : COLON INTEGER'
    p[0] = (p[1], p[2])

def p_indexRange_toEnd(p):
    'indexRange : INTEGER COLON'
    p[0] = (p[1], p[2])

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
                | indexedId
                | numExpression 
                | BOOLEAN
                | list
                | listDimension'''
    p[0] = p[1]

def p_multipleAssignment(p):
    'multipleAssignment : ID COMMA idList ASSIGN varValue COMMA varValueList SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_idList_one(p):
    'idList : ID'
    p[0] = p[1]

def p_idList_many(p):
    'idList : ID COMMA idList'
    p[0] = (p[1], p[2], p[3])

def p_varValueList_one(p):
    'varValueList : varValue'
    p[0] = p[1]

def p_varValueList_many(p):
    'varValueList : varValue COMMA varValueList'
    p[0] = (p[1], p[2], p[3])