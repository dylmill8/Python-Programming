#Dylan Miller

#This program creates a class creates an array that stores 2 stacks
#that when combined have a max length of n

class TwoStacks:
    """class creates an array that stores 2 stacks
that when combined have a max length of n"""

    #n - saves the maximum length of the entire array (both stacks combined)
    #self.array - stores both stacks as a list
    #self.len1 & self.len2 - tracks the length of each individual stack
    def __init__(self,n):
        self.maxLen = n
        self.array = []
        self.len1 = 0
        self.len2 = 0

    #returns the height of the given stack
    def height(self,stackNum):
        """returns the height of the stack"""
        if stackNum == 1:
            return self.len1
        else: return self.len2

    #adds an item to the head/top of the given stack
    def push(self,stackNum,item):
        """adds an item to the head/top of the given stack"""
        #checking if the array is at the maximum length
        if len(self.array)<self.maxLen:
            #stack1 is added from the right, stack2 is added from the left
            if stackNum == 1:
                self.array = self.array + [item]
                self.len1 += 1
            else:
                self.array = [item] + self.array
                self.len2 += 1
        else: print("ERROR: The stack is full!")

    #deletes and returns the top item in a given stack
    def pop(self,stackNum):
        """deletes and returns the top item in a given stack"""
        if stackNum == 1 and self.len1>0:
            #pops the top item (index = length -1) and
            #reduces the length of the stack
            item = self.array.pop(len(self.array)-1)
            self.len1 -= 1
            return item
        elif stackNum == 2 and self.len2>0:
            item = self.array.pop(0)
            self.len2 -= 1
            return item
        #if the stack you try to pop from is empty then prints and error
        else: print("ERROR: The stack is empty!")

    #prints the full array with both stacks
    def __str__(self):
        array = ""
        for i in self.array:
            array = array+str(i)+" "
        return str(array)
