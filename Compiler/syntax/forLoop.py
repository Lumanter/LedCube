
# For loop
def p_forLoop(p):
    'forLoop : FOR ID IN iterable LBRACE statementList RBRACE SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_forLoop_step(p):
    'forLoop : FOR ID IN iterable STEP INTEGER LBRACE statementList RBRACE SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

def p_iterable(p):
    '''iterable : ID 
                | indexedId
                | INTEGER'''
    p[0] = p[1]
