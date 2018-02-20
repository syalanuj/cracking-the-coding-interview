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


class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    def traverseList(head):
        """Traversing a linked list from head and return count
            Time Complexity O(n) - traversing the whole list
            Space Complexity O(1) - single temp variable current
         """
        current = head
        while(current != None):
            print(current.data)
            current = current.getNext()
    def length(self):
        current = self.head
        count = 0 #count total nodes
        while(current != None):
            count += 1
            current = current.getNext()
        return count
    def insertBeginning(self,data):
        """ Insert new node at begining of lineked list
            O(1) complexity
        """
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(self.head)
        self.head = newNode
    def insertEnd(self,data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode
    def insertAtPos(self,data,pos):
        if(pos < 0 and pos > self.length()):
            return None
        elif(pos == 0):
            self.insertBeginning(data)
        elif(pos == self.length()):
            self.insertEnd(data)
        else:
            newNode = Node()
            newNode.setData(data)
            current = self.head
            count = 0
            while(count < pos - 1):
                count +=1
                current = current.getNext()

            newNode.setNext(current.getNext)
            current.setNext(newNode)
        def deleteAtBegining(self):
            if(self.length() == 0):
                print("Empty List")
            else:
                self.head = self.head.getNext()

        def deleteAtEnd(self):
            if(self.length() == 0):
                print("Empty List")
            else:
                prev_node = self.head
                curr_node = self.head
                while(curr_node.getNext() != None):
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                prev_node.setNext(None)

        def deleteValue(self,value):
            if(self.length() == 0):
                print("Empty List")
            else:
                prev_node = self.head
                curr_node = self.head
                while(curr_node.getNext() != None and curr_node.getData() != value):
                    if(curr_node.getData() == value):
                        prev_node.getNext() = curr_node.getNext()
                    else:
                        prev_node = curr_node
                        curr_node = curr_node.getNext()

                print("Value is not present")
