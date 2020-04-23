from symbolTable import *
def fun(tree):
    symbolTable = SymbolTable()
    children = tree.getSons()
    if not processConfigConstants(children[0], symbolTable):
        return False
    if not processVariables(children[1], symbolTable):
        return False
    return True

def processConfigConstants(configBranch, symbolTable):
    lookupList = ['timer', 'timeUnit', 'rows', 'columns', 'cube']
    for son in configBranch.getSons():
        for keyword in lookupList:
            name = son.getName()
            if name == keyword:
                tempValue = son.getSons()[2].getName()
                tempSymbol = Symbol(son.getName(), tempValue, "Reserved", "global")
                symbolTable.add(tempSymbol)
                break
            elif keyword == lookupList[-1]:
                return False
    return True

def processVariables(statementBranch, symbolTable):
    scope = "global"

    for node in statementBranch.getSons():
        if node.getName() == "procedureDeclaration":
            procedureDeclaration(node, symbolTable)
        elif node.getName() == "varAssignment":
            varAssignment(node, symbolTable, scope)
        elif node.hasSons():
            processVariables(node, symbolTable)

    return True


def statement(node, symbolTable, scope):
    tempNode = node.getSon(0)

    if tempNode.getName() == "procedureDeclaration":
        procedureDeclaration(tempNode, symbolTable)
    if tempNode.getName() == "varAssignment":
        varAssignment(tempNode, symbolTable, scope)
    if tempNode.getName() == "procedureCall":
        #procedureCall(node, symbolTable)
        pass
    if tempNode.getName() == "builtInFunction":
        #procedureDeclaration(node, symbolTable)
        pass


def statementList(node, symbolTable, scope):

    for tempNode in node.getSons():
        if tempNode.getName() == "statement":
            statement(tempNode, symbolTable, scope)
        if tempNode.getName() == "statementList":
            statementList(tempNode, symbolTable, scope)

def procedureDeclaration(node, symbolTable):
    scope = node.getSon(1).getName()

    for tempNode in node.getSons():
        if tempNode.getName() == "statementList":
            statementList(tempNode, symbolTable, scope)


def numExpression(value, symbolTable, scope, varID):
    if value.hasSons():
        numExpression(value.getSon(0), symbolTable, scope, varID)
    else:
        tempValue = int(value.getName())
        if not symbolTable.hasSymbolByScope(varID, scope):
            tempSymbol = Symbol(varID, tempValue, Types.Integer, scope)
            symbolTable.add(tempSymbol)
        else:
            return False


def listElements(valueNode, symbolTable, scope, varID, tempFinalValue):

    isFinal = True

    for child in valueNode.getSons():
        if child.getName() == "listElement":
            tempElement = str(child.getSon(0).getName())
            tempFinalValue += tempElement + ','
        if child.getName() == "listElements":
            isFinal = False
            listElements(child, symbolTable, scope, varID, tempFinalValue)

    if isFinal:
        tempFinalValue = '[' + tempFinalValue[:-1] + ']'
        tempSymbol = Symbol(varID, tempFinalValue, Types.List, scope)
        symbolTable.add(tempSymbol)






def list_process(valueNode, symbolTable, scope, varID):
    elements = valueNode.getSon(1)
    tempFinalValue = ""
    listElements(elements, symbolTable, scope, varID, tempFinalValue)


def varValue(valueNode, symbolTable, scope, varID):
    value = valueNode.getSon(0)
    varValueType = value.getName()
    if varValueType == "numExpression":
        numExpression(value, symbolTable, scope, varID)
    if varValueType == "list":
        list_process(value, symbolTable, scope, varID)
    # if varValueType == "ID":
    #     #add symbol for ID
    # if varValueType == "BOOLEAN":
    #     #add symbol for BOOLEAN


def simpleAssignment(tempNode, symbolTable, scope):
    varID = tempNode.getSon(0).getName()
    valueNode = tempNode.getSon(2)
    varValue(valueNode, symbolTable, scope, varID)


def varAssignment(node, symbolTable, scope):
    tempNode = node.getSons()[0]
    if tempNode.getName() == "simpleAssignment":
        simpleAssignment(tempNode, symbolTable, scope)
    # if tempNode.getName() == "indexAssignment":
    #     #indexAssignment(tempNode, symbolTable, scope)