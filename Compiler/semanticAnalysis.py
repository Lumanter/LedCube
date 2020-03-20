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
            son4 = self.son4.translation()
        if type(self.son4) == type(type(tuple)):
            son4 = self.son4[0].translation()
        else:
            son4 = self.son4.translation()
        if type(self.son5) == type(type(tuple)):
            son5 = self.son5[0].translation()
        else:
            son5 = self.son5.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        tree += id + "->" + son5 + "\n\t"


        print tree
        return id

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

        tree += str(id) + "->" + son1 + "\n\t"
        print tree

        tree += str(id) + "->" + son2 + "\n\t"
        print tree

        tree += str(id) + "->" + str(son3) + "\n\t"
        print tree

        tree += str(id) + "->" + son4 + "\n\t"
        print tree


        return id

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

        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"


        print tree
        return id

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

        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"


        print tree
        return id

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

        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"


        print tree
        return id

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

        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"


        print tree
        return id

class statementList_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

class statementList_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translation()
        son2 = self.son2[0].translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"


        print tree
        return id

class statementList_empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

class statement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

class varAssignment(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1[0].translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

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

        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3[0].translation()
        son4 = self.son4.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"


        print tree
        return id

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

        son1 = self.son1.translation()
        son2 = self.son2[0].translation()
        son3 = self.son3.translation()
        son4 = self.son4[0].translation()
        son5 = self.son5.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"

        tree += id + "->" + son4 + "\n\t"

        tree += id + "->" + son5 + "\n\t"


        print tree
        return id

class index_one(Node):
    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()
        son2 = self.son2[0].translation()
        son3 = self.son3.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"

        tree += id + "->" + son3 + "\n\t"


        print tree
        return id

class index_many(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()
        son2 = self.son2.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"

        tree += id + "->" + son2 + "\n\t"


        print tree
        return id

class indexValue(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

class varValue(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1
    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
        return id

class builtInFunction(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translation(self):
        global tree
        id = increaseCount()

        son1 = self.son1.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"

        tree += id + "->" + son1 + "\n\t"


        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()
        son5 = self.son5.translation()
        son6 = self.son6.translation()
        son7 = self.son7.translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        tree += id + "->" + son7 + "\n\t"

        print tree
        return id

class list_empty(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2[0].translation()
        son3 = self.son3.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"

        print tree
        return id

class listElements_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
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
        son1 = self.son1[0].translation()
        son2 = self.son2.translation()
        son3 = self.son3[0].translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"

        print tree
        return id

class listElement(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class numExpression_plus(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class numExpression_minus(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class numExpression_uminus(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class term_multiply(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class term_divide(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class term_modulo(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class term_power(Node):
    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class numExpression_term(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class term_factor(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class factor_integer(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()
        son5 = self.son5.translation()
        son6 = self.son6[0].translation()
        son7 = self.son7.translation()
        son8 = self.son8.translation()


        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"
        tree += id + "->" + son7 + "\n\t"
        tree += id + "->" + son8 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4[0].translation()
        son5 = self.son5.translation()
        son6 = self.son6.translation()
        son7 = self.son7[0].translation()
        son8 = self.son8.translation()
        son9 = self.son9.translation()


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

        print tree
        return id

class parameters_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()
        
        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
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
        son1 = self.son1[0].translation()
        son2 = self.son2.translation()
        son3 = self.son3[0].translation()

        tree += id + "[label= " + self.name + "]" + "\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"

        print tree
        return id

class parameter(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1.translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4.translation()
        son5 = self.son5.translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"

        print tree
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
        son1 = self.son1.translation()
        son2 = self.son2.translation()
        son3 = self.son3.translation()
        son4 = self.son4[0].translation()
        son5 = self.son5.translation()
        son6 = self.son6.translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"
        tree += id + "->" + son4 + "\n\t"
        tree += id + "->" + son5 + "\n\t"
        tree += id + "->" + son6 + "\n\t"

        print tree
        return id

class arguments_one(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()

        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
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
        son1 = self.son1[0].translation()
        son2 = self.son2.translation()
        son3 = self.son3[0].translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"
        tree += id + "->" + son2 + "\n\t"
        tree += id + "->" + son3 + "\n\t"

        print tree
        return id

class argument(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()
        son1 = self.son1[0].translation()
        
        tree += id + "[label= "+self.name+"]"+"\n\t"
        tree += id + "->" + son1 + "\n\t"

        print tree
        return id

class empty(Node):
    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def translate(self,):
        global tree 
        id = increaseCount()

        tree += id + "[label= "+self.name+"]"+"\n\t"