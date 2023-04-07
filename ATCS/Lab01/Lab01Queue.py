#Dylan Miller

#Uses the TwoStack class to implement a queue where the first item
#in is the first one out

#imports the TwoStacks class
from Lab01TwoStacks import *

#creates a Queue class that can add items to the back of the queue
#and remove items from the front
class Queue(TwoStacks):
    """class that can add items to the back of the queue
and remove items from the front"""

    #n - saves the maximum length of the entire array (both stacks combined)
    #self.array - stores both stacks as a list
    #self.len1 & self.len2 - tracks the length of each individual stack
    def __init__(self,n):
        self.maxLen = n
        self.array = []
        self.len1 = 0
        self.len2 = 0

    #returns the length of the queue
    def length(self):
        """returns the length of the queue"""
        return int(len(self.array))

    #pushes and item to the head of the queue which will reverse order
    #when we need to dequeue from the stack
    def enqueue(self,item):
        """pushes and item to the back of the queue"""
        self.push(1,item)

    #dequeues the first item that was added to the queue
    def dequeue(self):
        """dequeues the first item that was added to the queue"""
        #moves everything from stack1 to stack2, thus reversing the order
        for i in range(self.height(1)):
            copy = self.pop(1)
            self.push(2,copy)
        #pops from the top of the new reversed stack
        #to get the first item that was queued
        item = self.pop(2)
        #moves everything from stack2 back to 1 to reset the queue
        for i in range(self.height(2)):
            copy = self.pop(2)
            self.push(1,copy)
        return item

    def __str__(self):
        array = ""
        for i in self.array:
            array = array+str(i)+" "
        return str(array)
