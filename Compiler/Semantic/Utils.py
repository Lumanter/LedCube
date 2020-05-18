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


def createCube(dimension, size, value):
    cube = []
    if dimension == 1:
        for index in range(size):
            cube.append(value)
    else:
        for index in range(size):
            cube.append(createCube(dimension - 1, size, value))
    return cube