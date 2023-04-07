#Dylan Miller

#this program creates a doubly linked list of max length n using
#a single array made from a python list

class DDLArray:
    """class creates a doubly linked list of max length n from an array"""

    #self.head - tracks the latest node added to the linked list
    #self.array - is a list containing all the nodes
    def __init__(self,n):
        self.head = None
        self.array = []

    #returns the first free node in the array
    def allocate(self):
        """returns the first free node in the array"""
        #iterates across the list checking each node to see if it
        #is free, and returns the index value if it is
        for i in range(len(self.array)):
            if self.freeNode(i) == True:
                return i
        #if there are no free nodes then an error is printed and returns None
        print("ERROR: The list is full")
        return None

    #returns True if there is no value stored at the given index of the array
    def freeNode(self,index):
        """determines if a node is empty or if there is already a value
at the given index of the array"""
        if self.array[index] == None:
            return True
        else: return False

    #adds a new item to the linked list and sets its forward and backward pointers
    def insert(self,item):
        """adds a new item to the linked list"""
        self.array = self.array + [None]
        #creates a node from the item ([back pointer,item value,forward pointer])
        item = [None,item,None]
        #if the array has no nodes, then it adds the first node and makes
        #it the head
        if self.head == None:
            self.array[0] = item
            self.head = item
        else:
            #makes the old head index the back pointer on the new node
            previous = self.array.index(self.head)
            item[0] = previous
            #finds the first free node
            freeNode = self.allocate()
            #returns if the list is full/no free nodes
            if freeNode == None:
                return
            else:
                #places the new node at the index of the free node
                self.array[freeNode] = item
                #sets the old head's forward pointer to the new node's index
                self.head[2] = self.array.index(item)
                #sets the new node as the new head
                self.head = item

    #finds the index of the first instance of an item
    def search(self,item):
        """finds the index of the first instance of an item"""
        for i in self.array:
            #makes sure to not include the None values
            #when iterating over the array
            if i != None:
                #if the value in the node is the same as the value
                #we are searching for then return the index of the node
                if i[1] == item:
                    return self.array.index(i)
        else:
            print("ERROR: Value not found")
            return None

    #deletes a node from the linked list
    def delete(self,item):
        """deletes a node from the linked list"""
        if self.head == None:
            print("Underflow error")
        else:
            #finds the index of the item we want to delete
            index = self.search(item)
            #saves the forward and back pointers
            forward = self.array[index][2]
            back = self.array[index][0]
            #sets the previous node's forawrd pointer to the forward node's index
            self.array[back][2] = forward
            #sets the forward node's back pointer to the previous node's index
            self.array[forward][0] = back
            #replaces the value we wish to delete with None so it will now
            #be marked as a free node
            self.array[index] = None

    #prints the items in the linked list from head to tail
    def __str__(self):
        elements = ""
        item = self.head
        #iterates through the list to get the length (I chose not to use len
        #so that I can exclude the None placeholder values)
        for i in self.array:
            #if there is a none value then i will pass over it, effectively not
            #counting any indices with none values as part of the length
            if i != None:
                elements = elements+str(item[1])+" "
                #stops when the back pointer of the current value
                #is none, meaning we have reached the tail end of the array
                if item[0] != None:
                    item = self.array[item[0]]
        return elements
