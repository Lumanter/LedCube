from variableChecker import *

tree = " "
count = 0


def increaseCount():
    global count
    count = count + 1
    return "%d" % count


class Node():
    def __init__(self, name):
        self.name = name
        self.sonList = []

    def getName(self):
        return self.name

    def hasSons(self):
        if len(self.sonList) == 0:
            return False
        return True

    def getSonsLength(self):
        counter = 0
        for son in self.sonList:
            counter += 1
        return counter

    def getSons(self):
        return self.sonList

    def getSon(self, index):
        return self.sonList[index]

    def addChild(self, son):
        self.sonList.append(son)


class Null(Node):
    def __init__(self, sonList):
        self.type = 'void'
        self.sonList = []

    def imprimir(self, ident):
        print ident + "nodo nulo"


# def processTree(Tree):
# Variable checks:
# Scope Resolution
# Type
# Multiple declaration of variable in same scope
# Reserve Identifier misuse
# Undeclare Variable
# index access
# loop checking

class program(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList
        self.translation()

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        print tree

        return fun(tempNode)


class configurationConstants(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class timer(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class timeUnit(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class rows(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class columns(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class cube(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class statementList_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class statementList_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class statementList_empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class statement(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class varAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class simpleAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class indexAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class index_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class index_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class indexValue(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


# Special Case #1
class varValue(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class builtInFunction(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class delay_default(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class delay_custom(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class list_empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class list(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class listElements_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class listElements_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


# Special case#2
class listElement(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class numExpression_plus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class numExpression_minus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class numExpression_uminus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class term_multiply(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class term_divide(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class term_modulo(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class term_power(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class numExpression_term(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class term_factor(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class factor_integer(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class procedureDeclaration_noParameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class procedureDeclaration_parameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class parameters_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class parameters_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class parameter(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class procedureCall_noParameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class procedureCall_parameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class arguments_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class arguments_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class argument(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode


class empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self, ):
        global tree
        id = increaseCount()

        tempNode = Node(self.name)

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        return tempNode
