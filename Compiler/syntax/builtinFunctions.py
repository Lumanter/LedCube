
# Built-in Functions 
def p_builtInFunction(p):
    '''builtInFunction : delay
                       | listOperation'''
    p[0] = p[1]

# Delay 
def p_delay_default(p):
    'delay : DELAY LPARENTHESES RPARENTHESES SEMICOLON'
    p[0] = (p[1], p[2], p[3])

def p_delay_custom(p):
    'delay : DELAY LPARENTHESES INTEGER COMMA TIMEUNIT RPARENTHESES SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])

# Matrix Shape Function
# - referenced within p_varValue, inside variableAssignments
def p_listDimension(p):
    'listDimension : ID LISTDIMENSION'
    p[0] = (p[1], p[2])

# List T/F/Neg operations
def p_listOperation(p):
    'listOperation : ID index LISTOPERATOR SEMICOLON'
    p[0] = (p[1], p[2], '.', p[3])

# List Delete Function
def p_listDelete(p):
    'listDelete : ID DELETE LPARENTHESES INTEGER RPARENTHESES SEMICOLON'
    p[0] = (p[1], '.', p[2], p[3], p[4], p[5])

def p_listDelete_eliminationType(p):
    'listDelete : ID DELETE LPARENTHESES INTEGER COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7])


# List Insert Function
def p_listInsert_one(p):
    'listInsert : ID INSERT LPARENTHESES INTEGER COMMA BOOLEAN RPARENTHESES SEMICOLON'
    p[0] = (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7])

def p_listInsert_many(p):
    'listInsert : ID INSERT LPARENTHESES list COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7])

def p_listInsert_many_atIndex(p):
    'listInsert : ID INSERT LPARENTHESES list COMMA INTEGER COMMA INTEGER RPARENTHESES SEMICOLON'
    p[0] = (p[1], '.', p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])

