
# Name: Reilly Sheehan

# This module will import TwoStacks and contain the class Queue. A queue will
# add items to the tail of the queue and remove them from the head.

from Lab01TwoStacks import *

class Queue():
    "a list of elements that follows FIFO"

    def __init__(self,n):
        "an instance of TwoStacks will be created"
        # Store max
        self.max = n
        # Create a TwoStacks
        self.stacks = TwoStacks(n)
        # Store current stack variable: 1 is Enqueue form, 2 is Dequeue form
        self.current = 1


    def length(self):
        "returns length of queue"
        return self.stacks.height(self.current)


    def enqueue(self,item):
        "adds item to tail of queue"
        # Check for form
        self.checkForm(1)
        # Push item to current stack
        self.stacks.push(self.current,item)


    def dequeue(self):
        "returns and removes first item in the queue"
        # Check form
        self.checkForm(2)
        # Dequeue item and return
        return self.stacks.pop(self.current)


    def checkForm(self,x):
        "checks if stack is in proper form for enqueueing or dequeueing and\
rearranges stack if not"
        # If x and self.current match, stack is in proper form and nothing needs
        # to be done
        if x != self.current:
            # Store variable for opposite stack
            if self.current == 1:
                opp = 2
            else:
                opp = 1
            # Itereate through current stack and push the pop onto opposite
            # stack
            for i in range(self.length()):
                self.stacks.push(opp,self.stacks.pop(self.current))
            # Update self.current variable
            self.current = opp
