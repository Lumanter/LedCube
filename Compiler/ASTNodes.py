from semanticAnalysis import *

tree = "\t"
count = 0


def increaseCount():
    global count
    count = count + 1
    return "%d" % count


class ASTNode():
    def __init__(self, name, sons):
        self.name = name
        self.sonList = sons

    def getName(self):
        return self.name

    def hasSons(self):
        if len(self.sonList) == 0:
            return False
        return True

    def getSonsLength(self):
        counter = 0
        for son in self.sonList:
            counter += 1
        return counter

    def getSons(self):
        return self.sonList

    def getSon(self, index):
        return self.sonList[index]

    def addChild(self, son):
        self.sonList.append(son)

    def translation(self):
        global tree
        id = increaseCount()

        tempNode = ASTNode(self.name, [])

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(ASTNode(son.getName(), []))
            else:
                tempNode.addChild(ASTNode(son, []))

        return tempNode


class program(ASTNode):
    def __init__(self, name, sonList):
        self.name = name
        self.sonList = sonList
        self.translation()

    def translation(self):
        global tree
        global count
        tree = "\t"
        count = 0
        id = increaseCount()

        tempNode = ASTNode(self.name, [])

        tree += id + "[label= " + self.name + "]" + "\n\t"

        for son in self.sonList:
            if (type(son) != str) and (type(son) != int) and (type(son) != bool):
                if son.hasSons():
                    tempNode.addChild(son.translation())
                else:
                    tempNode.addChild(Node(son.getName()))
            else:
                tempNode.addChild(Node(son))

        print tree

        return findVariables(tempNode)
