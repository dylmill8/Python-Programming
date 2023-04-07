#Dylan Miller

#this program uses two classes to create a circular
#doubly linked list 

#creates a node that stores a value, previous pointer, and forward pointer
class Link:
    """creates a node that stores a value, previous pointer, and forward pointer"""

    #self.previous - tracks the previous node in the linked list
    #self.next - tracks the next node in the linked list
    #self.value - stores the item value
    def __init__(self,value):
        self.previous = None
        self.next = None
        self.value = value

    #returns the value stored in the node
    def getValue(self):
        """returns the value stored in the node"""
        return self.value

    #returns the forward pointer stored in the node
    def getNext(self):
        """returns the forward pointer stored in the node"""
        return self.next

    #returns the previous pointer stored in the node
    def getPrevious(self):
        """returns the previous pointer stored in the node"""
        return self.previous

    #sets a new forward pointer
    def setNext(self,newNext):
        """sets a new forward pointer"""
        self.next = newNext

    #sets a new previous pointer
    def setPrevious(self,newPrevious):
        """sets a new previous pointer"""
        self.previous = newPrevious

#stores and manages the links in the linked list
class CircDoubLinkedList:
    """stores and manages the links in the linked list"""

    #self.head - tracks the latest node added to the linked list
    #self.tail - tracks the first node added to the linked list
    #self.length - tracks the length of the items in the linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #adds a new link to the linked list
    def insert(self,value):
        """adds a new link to the linked list"""
        #creates the link object
        link = Link(value)
        #if the list is empty then adds the node to the list
        #and sets it as both the head and tail
        if self.head == None:
            self.head = link
            self.tail = link
            self.length += 1
        else:
            #sets the forward pointer to the tail to make the list circular
            link.setNext(self.tail)
            #sets the previous to the old head value
            link.setPrevious(self.head)
            #sets the old head forward pointer to the new link
            self.head.setNext(link)
            #sets the head as the new link
            self.head = link
            #sets the tail's previous pointer to the new link
            self.tail.setPrevious(self.head)
            self.length += 1

    #searches for the first value in the linked list
    def search(self,value):
        """searches for the first value in the linked list"""
        old = None
        new = self.head
        #starts with the head and iterates through the list
        for i in range (self.length):
            old,new = new,new.getNext()
            #once the value is found, the previous is stored as old, and
            #the value we are looking for is stored as new
            if new.getValue() == value:
                return old,new
        return print("No link with that value")

    #deltes a link from the list
    def delete(self,value):
        """deltes a link from the list"""
        if self.head == None:
            print("Underflow error")
        else:
            try:
                #searches for the value to delete
                old,new = self.search(value)
                #sets the previous node to the forward node, effectively cutting
                #out the value in the middle
                old.setNext(new.getNext())
                #sets the forward node to the previous node, effectively cutting
                #out the value in the middle
                new.getNext().setPrevious(old)
                self.length -= 1
                #if the head is the value being deleted then set the head to the
                #node thay comes before
                if self.head.getValue() == value:
                    self.head = old
            except: return

    #prints the linked list from head to tail
    def __str__(self):
        linkedList = ""
        item = self.head
        for i in range (self.length):
            linkedList = linkedList+str(item.getValue())+" "
            #tracks backwards from head to tail using previous pointers
            item = item.getPrevious()
        return str(linkedList)
