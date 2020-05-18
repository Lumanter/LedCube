class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNext(self, node):
        self.nextNode = node

    def getNext(self):
        return self.nextNode

    def getValue(self):
        return self.value