from symbolTable import *
from codeRunner import searchNodeByName
from codeGenerator import delay

readyForRun = False
code = None


def fun(tree):
    global code
    code = tree
    symbolTable = SymbolTable()
    children = tree.getSons()
    if not processConfigConstants(children[0], symbolTable):
        return False
    if not processVariables(children[1], symbolTable):
        return False
    processSimulationOfCode(children[1], symbolTable)
    return True


def processSimulationOfCode(tree, symbolTable):
    global readyForRun
    readyForRun = True

    tempNode = searchNodeByName(tree, "main")
    procedureDeclaration(tempNode, symbolTable)


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


def procedureCall(node, symbolTable):
    global code
    tempCode = code.getSons()[1]
    functionName = node.getSon(0).getSon(1).getName()
    tempNode = searchNodeByName(tempCode, functionName)
    procedureDeclaration(tempNode, symbolTable)


def getAttributes(functionNode):
    attributes = []
    tempList = functionNode.getSons()[2:-2]
    for attribute in tempList:
        tempName = attribute.getName()
        if tempName != ',':
            attributes.append(tempName)
    return attributes


def delayFunction(tempNode, symbolTable):
    if readyForRun:
        attributes = getAttributes(tempNode)
        if len(attributes) != 0:
            delay(attributes[0], attributes[1])
        else:
            tempSymbolTime = symbolTable.getSymbol("timer").getByIndex(0).getValue()
            tempSymbolTimeUnit = symbolTable.getSymbol("timeUnit").getByIndex(0).getValue()
            delay(str(tempSymbolTime.getValue()), str(tempSymbolTimeUnit.getValue()))


def builtInFunction(node, symbolTable):
    tempNode = node.getSon(0)
    tempName = tempNode.getName()

    if tempName == "delay":
        delayFunction(tempNode, symbolTable)


def statement(node, symbolTable, scope):
    tempNode = node.getSon(0)

    if tempNode.getName() == "procedureDeclaration":
        procedureDeclaration(tempNode, symbolTable)
    if tempNode.getName() == "varAssignment":
        varAssignment(tempNode, symbolTable, scope)
    if tempNode.getName() == "procedureCall":
        procedureCall(node, symbolTable)
    if tempNode.getName() == "builtInFunction":
        builtInFunction(tempNode, symbolTable)
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


def listElement(element):
    tempNode = None
    elementType = element.getName()
    if elementType == "listElement":
        tempNode = Node(element.getSon(0).getName())
    elif elementType == "listElements":
        if element.getSonsLength() == 1:
            tempNode = Node(element.getSon(0).getSon(0).getName())
        else:
            tempNode = Node(listElements(element))
    return tempNode


def listElements(elements):
    tempLinkedList = LinkedList()

    for child in elements.getSons():
        tempNode = listElement(child)
        if tempNode != None:
            tempLinkedList.add(tempNode)

    return tempLinkedList


def list_process(valueNode, symbolTable, scope, varID):
    elements = valueNode.getSon(1)
    newValue = listElements(elements)
    tempSymbol = Symbol(varID, newValue, Types.List, scope)
    symbolTable.add(tempSymbol)


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
