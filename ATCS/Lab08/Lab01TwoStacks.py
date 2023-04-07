
# Name: Reilly Sheehan

# This module will contain the class TwoStacks. Each instance will consist of
# two stacks within an array and have methods to push, pop, and return the
# height and elements.


class TwoStacks():
    "two stacks within an array"

    def __init__(self,n):
        "creates two stacks within an array length n."
        # Create variable for max
        self.max = int(n)
        # Create list and add None so that list contains max elements
        self.list = []
        for i in range(self.max):
            self.list.append(None)
        # Create lists of heads and tails
        self.heads = []
        self.tails = []
        # Assign heads and tails of each stack
        self.heads.append(0)
        self.tails.append(0)
        self.heads.append(-1)
        self.tails.append(-1)


    def height(self,stackNum):
        "returns the height of stack #stackNum."
        # Get index value:
        x = stackNum-1
        # Detemine whether tail is before or after head and then find height by
        # finding difference between head and tail
        if stackNum == 1:
            height = (self.tails[x] - self.heads[x])
        else:
            height = -1*(self.tails[x] - self.heads[x])

        return height
                

    def push(self,stackNum,item):
        "adds item to top of stack #stackNum or prints error if limit reached."
        # Check if list has reached max elements
        if self.height(1) + self.height(2) == self.max:
            print("Overflow error: limit reached")
        else:
            # Get index values
            x = stackNum - 1
            # Assign empty list spot to item and re-assign tail values
            self.list[self.tails[x]] = item
            if x == 0:
                self.tails[x] += 1
            else:
                self.tails[x] -= 1


    def pop(self,stackNum):
        "removes top item from stack #stackNum and returns it."
        # Check if there are any items to pop
        if self.height(stackNum) == 0:
            print("Underflow error: there are no elements in stack "+\
                  str(stackNum))
        else:
            # Get index
            x = stackNum - 1
            # Number to add to index value
            if stackNum == 1:
                dif = -1
            else:
                dif = 1
            # Find item in list
            item = self.list[self.tails[x]+dif]
            # Replace item with None
            self.list[self.tails[x]+dif] = None
            # Adjust tail
            self.tails[x] = self.tails[x] + dif

            return item


    def __str__(self):
        "returns a string containing all elements in the array"
        # Remove None values
        string = []
        for i in self.list:
            if i != None:
                string.append(i)
        return string
