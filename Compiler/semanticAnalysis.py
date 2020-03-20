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

	def translation(self):
		global tree
		id = increaseCount()
		tree += id+"[label= "+"nodo_nulo"+"]"+"\n\t"


		print tree
		return id


class program(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self):
        global tree
        id = increaseCount()

        print (type(self.son1))

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        return "AST {\n\t"+tree+"}"

class configurationConstants(Node):
    def __init__(self, name, son1, son2, son3, son4, son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()
        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()
        if type(self.son4) == type(type(tuple)):
            son4 = self.son4[0].translation()
        else:
            son4 = self.son4.translation()
        if type(self.son5) == type(type(tuple)):
            son5 = self.son5[0].translation()
        else:
            son5 = self.son5.translation()

        tree += str(id) + "[label= " + self.name + "]" + "\n\t"

        tree += str(id) + "->" + str(son1) + "\n\t"

        tree += str(id) + "->" + str(son2) + "\n\t"

        tree += str(id) + "->" + str(son3) + "\n\t"

        tree += str(id) + "->" + str(son4) + "\n\t"

        tree += str(id) + "->" + str(son5) + "\n\t"


        print tree
        return str(id)

class timer(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4

        tree += str(id) + "[label= " + self.name + "]" + "\n\t"
        print tree

        tree += str(id) + "->" + str(son1) + "\n\t"
        print tree

        tree += str(id) + "->" + str(son2) + "\n\t"
        print tree

        tree += str(id) + "->" + str(son3) + "\n\t"
        print tree

        tree += str(id) + "->" + str(son4) + "\n\t"
        print tree


        return str(id)

class timeUnit(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"


        print tree
        return str(id)

class rows(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"


        print tree
        return str(id)

class columns(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"


        print tree
        return str(id)

class cube(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()
        son4 = self.son4

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"


        print tree
        return str(id)

class statementList_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class statementList_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"


        print tree
        return str(id)

class statementList_empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class statement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class varAssignment(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()
        
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class simpleAssignment(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        son2 = self.son2
        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()
        son4 = self.son4

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"


        print tree
        return str(id)

class indexAssignment(Node):
    def __init__(self, name, son1, son2, son3, son4, son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()

        son3 = self.son3
        if type(self.son4) == type(type(tuple)):
            son4 = self.son4[0].translation()
        else:
            son4 = self.son4.translation()
        son5 = self.son5

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"

        tree += id + "->" + str(son4) + "\n\t"

        tree += id + "->" + str(son5) + "\n\t"


        print tree
        return str(id)

class index_one(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()

        son3 = self.son3

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"

        tree += id + "->" + str(son3) + "\n\t"


        print tree
        return str(id)

class index_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"

        tree += id + "->" + str(son2) + "\n\t"


        print tree
        return str(id)

class indexValue(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

#Special Case #1
class varValue(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1
    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class builtInFunction(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + str(son1) + "\n\t"


        print tree
        return str(id)

class delay_default(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"

        print tree
        return str(id)

class delay_custom(Node):
    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4
        son5 = self.son5
        son6 = self.son6
        son7 = self.son7

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"
        tree += id + "->" + str(son5) + "\n\t"
        tree += id + "->" + str(son6) + "\n\t"
        tree += id + "->" + str(son7) + "\n\t"

        print tree
        return str(id)

class list_empty(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"

        print tree
        return str(id)

class list(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        if type(self.son2) == type(type(tuple)):
            son2 = self.son2[0].translation()
        else:
            son2 = self.son2.translation()
        son3 = self.son3
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"

        print tree
        return str(id)

class listElements_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class listElements_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self,):
        global tree 
        id = increaseCount()

        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        son2 = self.son2

        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"

        print tree
        return str(id)

#Special case#2
class listElement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class numExpression_plus(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class numExpression_minus(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class numExpression_uminus(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class term_multiply(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class term_divide(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class term_modulo(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class term_power(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class numExpression_term(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class term_factor(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class factor_integer(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class procedureDeclaration_noParameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7, son8):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

        
    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4
        son5 = self.son5
        if type(self.son6) == type(type(tuple)):
            son6 = self.son6[0].translation()
        else:
            son6 = self.son6.translation()

        son7 = self.son7
        son8 = self.son8


        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"
        tree += id + "->" + str(son5) + "\n\t"
        tree += id + "->" + str(son6) + "\n\t"
        tree += id + "->" + str(son7) + "\n\t"
        tree += id + "->" + str(son8) + "\n\t"

        print tree
        return str(id)

class procedureDeclaration_parameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7, son8, son9):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9


    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        if type(self.son4) == type(type(tuple)):
            son4 = self.son4[0].translation()
        else:
            son4 = self.son4.translation()
        
        son5 = self.son5
        son6 = self.son6
        if type(self.son7) == type(type(tuple)):
            son7 = self.son7[0].translation()
        else:
            son7 = self.son7.translation()

        son8 = self.son8
        son9 = self.son9


        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"
        tree += id + "->" + str(son5) + "\n\t"
        tree += id + "->" + str(son6) + "\n\t"
        tree += id + "->" + str(son7) + "\n\t"
        tree += id + "->" + str(son8) + "\n\t"
        tree += id + "->" + str(son9) + "\n\t"

        print tree
        return str(id)

class parameters_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class parameters_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        son2 = self.son2
        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"

        print tree
        return str(id)

class parameter(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class procedureCall_noParameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        son4 = self.son4
        son5 = self.son5
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"
        tree += id + "->" + str(son5) + "\n\t"

        print tree
        return str(id)

class procedureCall_parameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5, son6):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def translation(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1
        son2 = self.son2
        son3 = self.son3
        if type(self.son4) == type(type(tuple)):
            son4 = self.son4[0].translation()
        else:
            son4 = self.son4.translation()

        son5 = self.son5
        son6 = self.son6
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"
        tree += id + "->" + str(son4) + "\n\t"
        tree += id + "->" + str(son5) + "\n\t"
        tree += id + "->" + str(son6) + "\n\t"

        print tree
        return str(id)

class arguments_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class arguments_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()

        son2 = self.son2
        if type(self.son3) == type(type(tuple)):
            son3 = self.son3[0].translation()
        else:
            son3 = self.son3.translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"
        tree += id + "->" + str(son2) + "\n\t"
        tree += id + "->" + str(son3) + "\n\t"

        print tree
        return str(id)

class argument(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()
        if type(self.son1) == type(type(tuple)):
            son1 = self.son1[0].translation()
        else:
            son1 = self.son1.translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + str(son1) + "\n\t"

        print tree
        return str(id)

class empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self,):
        global tree 
        id = increaseCount()

        tree += id + "[label= "+self.name+"]"+"\n\t"