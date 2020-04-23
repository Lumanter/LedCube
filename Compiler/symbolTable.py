import enum

class Types(enum.Enum):
    Boolean = "bool"
    Integer = "int"
    List = "list"

class Scopes(enum.Enum):
    Local = "local"
    Global = "global"

class SymbolTable:
    def __init__(self):
        self.symbols = {}
    def add(self, newSymbol):
        self.symbols[newSymbol.id] = newSymbol
    def hasSymbol(self, id):
        return id in self.symbols
    def hasSymbolByScope(self, id, scope):
        for symbol in self.symbols:
            if self.symbols.get(symbol).getID() == id and self.symbols.get(symbol).getScope() == scope:
                return True
        return False
    def getSymbol(self, id):
        return self.symbols[id]

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



# Example
#symbolTable = SymbolTable()
#symbolTable.add(Symbol("x", True, Types.Boolean, Scopes.Global))
#symbolTable.add(Symbol("y", 5, Types.Integer, Scopes.Global))

# say we are trying to set a Integer to x, that type is newVariableType
#newVariableType = Types.Integer
#if(symbolTable.getSymbol("x").type != newVariableType):
    #print "that's some illegal semantic violation: cannot set integer value to boolean variable"

