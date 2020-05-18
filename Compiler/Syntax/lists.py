
import sys
sys.path.append("..")
from ASTNodes import ASTNode


def p_list_empty(p):
    'list : LSQUAREBRACKET RSQUAREBRACKET'
    p[0] = ASTNode("list", (p[1], p[2]))


def p_list(p):
    'list : LSQUAREBRACKET listElements RSQUAREBRACKET'
    p[0] = ASTNode("list", (p[1], p[2], p[3]))


def p_listElements_one(p):
    'listElements : listElement'
    p[0] = ASTNode("listElements", ([p[1]]))


def p_listElements_many(p):
    'listElements : listElement COMMA listElements'
    p[0] = ASTNode("listElements", (p[1], p[2], p[3]))


def p_listElement(p):
    '''listElement : BOOLEAN
                   | list'''
    p[0] = ASTNode("listElement", ([p[1]]))
