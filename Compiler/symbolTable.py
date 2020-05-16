import enum
from LinkedList import *


class Types(enum.Enum):
    Boolean = "bool"
    Integer = "int"
    List = "list"
    Undefined = "undefined"


class Scopes(enum.Enum):
    Local = "local"
    Global = "global"


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, newSymbol):
        if newSymbol.id in self.symbols.keys():
            tempList = self.symbols[newSymbol.id]
            tempNode = Node(newSymbol)
            tempList.add(tempNode)
            self.symbols[newSymbol.id] = tempList
        else:
            tempList = LinkedList()
            tempNode = Node(newSymbol)
            tempList.add(tempNode)
            self.symbols[newSymbol.id] = tempList



    def hasSymbol(self, id):
        return id in self.symbols

    def hasSymbolByScope(self, id, scope):
        if self.getSymbolByScope(id, scope) == None:
            return False
        return True

    def getSymbol(self, id):
        return self.symbols[id]

    def getSymbolByScope(self, id, scope):
        if id in self.symbols.keys():
            tempList = self.symbols[id]
            for index in range(tempList.getLength()):
                tempNode = tempList.getByIndex(index)
                tempSymbol = tempNode.getValue()
                if tempSymbol.getScope() == scope:
                    return tempSymbol
            return None
        return None

    def eliminateSymbolByScope(self, id, scope):
        tempList = self.symbols[id]

        for index in range(tempList.getLength()):
            tempNode = tempList.getByIndex(index)
            tempSymbol = tempNode.getValue()
            if tempSymbol.getScope() == scope:
                tempList.deleteByIndex(index)
                break


    def modifySymbol(self, newSymbol):
        tempID = newSymbol.getID()
        tempScope = newSymbol.getScope()

        if self.hasSymbol(tempID):
            self.eliminateSymbolByScope(tempID, tempScope)

            self.symbols[tempID].add(newSymbol)
        else:
            self.add(newSymbol)


class Symbol:
    def __init__(self, id, value, type, scope):
        self.id = id
        self.value = value
        self.type = type
        self.scope = scope

    def getID(self):
        return self.id

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def getScope(self):
        return self.scope

    def setValue(self, value):
        self.value = value

    def setType(self, type):
        self.type = type

# Example
# symbolTable = SymbolTable()
# symbolTable.add(Symbol("x", True, Types.Boolean, Scopes.Global))
# symbolTable.add(Symbol("y", 5, Types.Integer, Scopes.Global))

# say we are trying to set a Integer to x, that type is newVariableType
# newVariableType = Types.Integer
# if(symbolTable.getSymbol("x").type != newVariableType):
# print "that's some illegal semantic violation: cannot set integer value to boolean variable"
