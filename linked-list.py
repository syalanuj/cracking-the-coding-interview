"""
Cracking the coding interview
Chapter 2: Linked List
Python linked list implementation reference taken from
'Data structure and Algorithmic Thinking with python' - 'Narashima Karumanchi'
@author - anujsyal
"""
import math
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
        print("HEAD --> ")
        while(current != None):
            print(current.data)
            print(" --> ")
            current = current.getNext()
        print("NULL")
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
#-----------------------------------------------------------------------------#
# 2.1 Remove dups: Write code to remove duplicates from unsorted linked list
# FOLLOW UP: How would you solve if temprory buffer not available
# Solution 1
    def removeDups(self):
        """ Remove duplicates from unsorted linked list using dictionary
            Time Complexity - O(n)
            Space Complexit - O(n) -n number of distinct values stored in dict
        """
        data_dict = {}
        prev_node = self.head
        curr_node = self.head
        while(curr_node.getNext() != None):
            if(data_dict[curr_node.getData()] == True):
                #remove using pointers
                prev_node.setNext(curr_node.getNext())
            else:
                data_dict[curr_node.getData()] = True
            prev_node = curr_node
            curr_node = curr_node.getNext()
# Solution 2
    def removeDups2(self):
        """ Remove duplicates from unsorted linked list without using dict
            Time Complexity - O(n2)
            Space Complexit - O(1)#
        """
        temp_node = self.head
        prev_node = self.head
        while(temp_node.getNext() != None):
            curr_node = temp_node.getNext()
            while(curr_node.getNext() != None):
                if(temp_node.getData() == curr_node.getData()):
                    prev_node.setNext(curr_node.getNext())
                prev_node = curr_node
                curr_node = curr_node.getNext()
            temp_node = temp_node.getNext()
#-----------------------------------------------------------------------------#
# 2.2 Return Kth to last: Implement an algo to find the kth to last element o a
# linked list
# Solution 1
    def kthToLast(self,k):
        """ Find kth of Last element
            Time Complexity - O(n) where n is length of linked list
        """
        curr_node = self.head
        count = 0
        while(count < self.length() - k):
            count += 1
            curr_node = curr_node = getNext()
        return curr_node # or curr_node.getData()
#Solution2 - Implement with recursion
    def kthToLast2(self,node,k):
        if(node == None):
            return 0
        index = kthToLast2(node.getNext(),k) + 1
        if(index == k):
            print("kth to last element", node.getData())
        return index
#-----------------------------------------------------------------------------#
# 2.3 Delete middle node: Implement an algo to delete node in middle of singly
# linked list, not given the HEAD
# Solution 1
    def deleteAtNode(self,node):
        next_node = node.getNext()
        node.setData(next_node.getData())
        node.setNext(next_node.getNext())
#-----------------------------------------------------------------------------#
# 2.5 Sum List: You have two numbers represented by linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that
# the one's digit is head of list. Write an algo that returns sum of numbers
# generated by linked list
# Example: (7->1->6) + (5->9->2) = 617 + 295 = 912
# Solution 1

def getNumberInReverse(head):
    current = head
    count = 0
    num = 0
    while(current != None):
        num += current.getData() * math.pow(10,count)
        count +=1
    return num

def sumList(head1,head2):
    num1 = getNumberInReverse(head1)
    num2 = getNumberInReverse(head2)
    return num1 + num2
    
# Solution 2
def getLength(head):
    count = 0
    current = head
    while(current != None):
        count +=1
    return count
def getNumberInOrder(head):
    current = head
    count = getLength(head) - 1
    num = 0
    while(current != None):
        num += current.getData() * math.pow(10,count)
        count -=1
    return num
def sumList(head1,head2):
    num1 = getNumberInOrder(head1)
    num2 = getNumberInOrder(head2)
    return num1 + num2
