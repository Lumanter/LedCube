
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

# Matrix Shape
# - linked within p_varValue, inside variableAssignments
def p_listDimension(p):
    'listDimension : ID LISTDIMENSION'
    p[0] = (p[1], p[2])

# List T/F/Neg operations
def p_listOperation(p):
    'listOperation : ID index LISTOPERATOR SEMICOLON'
    p[0] = (p[1], p[2], '.', p[3])




