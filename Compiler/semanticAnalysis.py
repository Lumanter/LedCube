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

	def translate(self):
		global tree
		id = increaseCount()
		tree += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id


class program(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()

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

    def translate(self):
        global tree
        id = increaseCount()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        tree += id + "->" + son5 + "\n\t"

        return id

class timer(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class timeUnit(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class rows(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class columns(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class cube(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class statementList_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        return id

class statementList_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        return id

class statementList_empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        return id

class statement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        return id

class varAssignment(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        return id

class simpleAssignment(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3[0].translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class indexAssignment(Node):
    def __init__(self, name, son1, son2, son3, son4, son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2[0].translate()
        son3 = self.son3.translate()
        son4 = self.son4[0].translate()
        son5 = self.son5.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        tree += id + "->" + son5 + "\n\t"

        return id

class index_one(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2[0].translate()
        son3 = self.son3.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        return id

class index_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        return id

class indexValue(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        return id

class varValue(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2[0].translate()
        son3 = self.son3.translate()
        son4 = self.son4[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class builtInFunction(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        return id

class delay_default(Node):
    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        return id

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

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        tree += id + "->" + son7 + "\n\t"
        return id

class list_empty(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class list(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2[0].translate()
        son3 = self.son3.translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        return id

class listElements_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class listElements_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2.translate()
        son3 = self.son3[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        return id

class listElement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class numExpression_plus(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class numExpression_minus(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class numExpression_uminus(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class term_multiply(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class term_divide(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class term_modulo(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class term_power(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        return id

class numExpression_term(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class term_factor(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class factor_integer(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

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

        
    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6[0].translate()
        son7 = self.son7.translate()
        son8 = self.son8.translate()


        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        tree += id + "->" + son7 + "\n\t"
        tree += id + "->" + son8 + "\n\t"
        return id

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


    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4[0].translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7[0].translate()
        son8 = self.son8.translate()
        son9 = self.son9.translate()


        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        tree += id + "->" + son7 + "\n\t"
        tree += id + "->" + son8 + "\n\t"
        tree += id + "->" + son9 + "\n\t"
        return id

class parameters_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class parameters_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2.translate()
        son3 = self.son3[0].translate()

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        return id

class parameter(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class procedureCall_noParameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        return id

class procedureCall_parameters(Node):
    def __init__(self, name, son1, son2, son3, son4, son5, son6):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4[0].translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        return id

class arguments_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()

        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class arguments_many(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        son2 = self.son2.translate()
        son3 = self.son3[0].translate()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        return id

class argument(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translate()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        return id

class empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()

        tree += id + "[label= "+self.name+"]"+"\n\t"