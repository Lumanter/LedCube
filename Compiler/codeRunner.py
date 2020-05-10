def searchNodeByName(tree, name):
    tempList = tree.getSons()
    tempNode = None
    for son in tempList:
        if son.getName() == "procedureDeclaration":
            tempNodeList = son.getSons()
            for nodeSon in tempNodeList:
                if nodeSon.getName() == name:
                    tempNode = son
        elif son.hasSons():
            tempResult = searchNodeByName(son, name)
            if tempResult != None:
                return tempResult
        if tempNode != None:
            return tempNode
    return None
