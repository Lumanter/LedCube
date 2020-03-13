import enum

class Types(enum.Enum):
    Boolean = "bool"
    Integer = "int"

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
    def getSymbol(self, id):
        return self.symbols[id]

class Symbol:
  def __init__(self, id, value, type, scope):
    self.id = id
    self.value = value
    self.type = type
    self.scope = scope

# Example
symbolTable = SymbolTable()
symbolTable.add(Symbol("x", True, Types.Boolean, Scopes.Global))
symbolTable.add(Symbol("y", 5, Types.Integer, Scopes.Global))

# say we are trying to set a Integer to x, that type is newVariableType
newVariableType = Types.Integer
if(symbolTable.getSymbol("x").type != newVariableType):
    print "that's some illegal semantic violation: cannot set integer value to boolean variable"

