
# If statement
def p_ifStatement(p):
    'ifStatement : IF varValue COMPARATOR comparisonValue LBRACE statementList RBRACE SEMICOLON'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_comparisonValue(p):
    '''comparisonValue : BOOLEAN 
                       | INTEGER'''
    p[0] = p[1]