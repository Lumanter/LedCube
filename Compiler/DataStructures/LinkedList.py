from Node import *

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, element):
        if self.length == 0:
            self.head = element
            self.tail = element
        else:
            self.tail.setNext(element)
            self.tail = element
        self.length += 1

    def getByIndex(self, index):
        current = self.head
        for counter in range(self.length):
            if counter == index:
                return current
            current = current.getNext()
        return None

    def deleteByIndex(self, index):
        if index == 0:
            temp = self.head.getNext()
            self.head = temp
        elif index == (self.length - 1):
            temp = self.getByIndex(self.length - 2)
            self.tail = temp
        elif (index > 0) and (index < (self.length - 1)):
            self.getByIndex(index - 1).setNext(self.getByIndex(index + 1))
        self.length -= 1

    def getLength(self):
        return self.length
