tree = " "
count = 0

def increaseCount():
    global count
    count = count + 1
    return "%d" %count

class Node():
    pass

class Null(Node):
	def __init__(self):
		self.type = 'void'

	def imprimir(self,ident):
		print ident + "nodo nulo"


class program(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return "AST {\n\t"+tree+"}"

class configurationConstants(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class timer(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class timeUnit(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class rows(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class columns(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class cube(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class statementList_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class statementList_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)

class statementList_empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class statement(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class varAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class simpleAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class indexAssignment(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class index_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class index_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class indexValue(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


#Special Case #1
class varValue(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList
    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class builtInFunction(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class delay_default(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class delay_custom(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class list_empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class list(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class listElements_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class listElements_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


#Special case#2
class listElement(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class numExpression_plus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class numExpression_minus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class numExpression_uminus(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class term_multiply(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class term_divide(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class term_modulo(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class term_power(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class numExpression_term(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class term_factor(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class factor_integer(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class procedureDeclaration_noParameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

        
    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class procedureDeclaration_parameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList


    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class parameters_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class parameters_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class parameter(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class procedureCall_noParameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class procedureCall_parameters(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class arguments_one(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class arguments_many(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class argument(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)


class empty(Node):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList

    def translation(self,):
        global tree
        id = increaseCount()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if type(son) == type(type(tuple)):
                tree += id + "->" + son.traslation() + "\n\t"
            else:
                tree += id + "->" + son + "\n\t"

        return str(id)
