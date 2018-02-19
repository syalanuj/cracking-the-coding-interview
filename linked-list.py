"""
Cracking the coding interview
Chapter 2: Linked List
Python linked list implementation reference taken from
'Data structure and Algorithmic Thinking with python' - 'Narashima Karumanchi'
@author - anujsyal
"""
#Basic python implementation of linked list
class Node(object):
    """Node of singly int linked list"""
    def __init__(self):
        self.data = None
        self.next = None
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None
