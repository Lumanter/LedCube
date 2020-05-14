def findNumValue(node):
    if node != None:
        if isinstance(node, int):
            return node
        if isinstance(node.getName(), int):
            return node.getName()
        tempList = node.getSons()
        for tempNode in tempList:
            findNumValue(tempNode)
    pass


def createCube(dimension, size):
    cube = []
    if dimension == 1:
        for index in range(size):
            cube.append(False)
    else:
        for index in range(size):
            cube.append(createCube(dimension - 1, size))
    return cube