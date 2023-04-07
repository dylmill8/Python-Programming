#Dylan Miller

#this program uses a queue to implement a simple time management game

from Lab01TwoStacks import *
from Lab01Queue import *
import random

#creates a Queue class that can add items to the back of the queue
#and remove items from the front
class Queue(Queue):
    """class that can add items to the back of the queue
and remove items from the front"""

    #dequeues the first item that was added to the queue
    def dequeue(self):
        """dequeues the first item that was added to the queue"""
        #moves everything from stack1 to stack2, thus reversing the order
        for i in range(self.height(1)):
            copy = self.pop(1)
            #only saves the customer if they have a patience higher than 0
            if copy > 0:
                self.push(2,copy)
            else: print("You lost a customer")
        #pops from the top of the new reversed stack
        #to get the first item that was queued
        item = self.pop(2)
        #moves everything from stack2 back to 1 to reset the queue
        for i in range(self.height(2)):
            copy = self.pop(2)
            self.push(1,copy)
        return item

    #returns the head of the queue
    def getHead(self):
        """returns the head of the queue"""
        return self.array[0]

    #sets the value of the item at index in the queue
    def setValue(self,index,value):
        """sets the value of the item at index in the queue"""
        self.array[index] = value

#plays the time management game until there are no customers left in the queue
#or the player chooses to quit
def playRound(queue,numCustomers,firstRound):
    playAgain = True
    while playAgain == True:
        #if there is room in the queue then there is a 50% chance to randomly
        #get a customer each round
        if queue.length() < numCustomers:
            chance = random.randint(1,2)
            #on the first time through, there is a guaranteed costomer
            if queue.length() == 0 and firstRound == True:
                randNum = random.randint(1,10)
                queue.enqueue(randNum)
                print("A customer is waiting (patience:",queue.getHead(),")")
                firstRound == False
            elif chance == 1:
                randNum = random.randint(1,10)
                queue.enqueue(randNum)
                print("A customer is waiting (patience:",queue.getHead(),")")
        action = 0
        while (action != 1) and (action != 2) and (action != 3):
            try:
                action = eval(input("(1) Seat customer\n(2) Wait\n(3) Quit\nAction (1,2,3): "))
            except:
                print("Invalid input")
        #if the player seats a customer then they are removed from the queue
        if action == 1:
            queue.dequeue()
            print("You sat a new customer")
        #if the player waits a customer then they are sent to the back
        #of the queue and their patience is reduced by 1
        elif action == 2:
            customer = queue.dequeue()
            queue.enqueue(customer-1)
        #quits if the queue is empty or the player ends the game
        elif action == 3:
            playAgain = False
        if queue.length() == 0:
            playAgain = False

def main():
    print("Welcome to Dylan's Doughnuts")
    print("The goal is to serve all of the customers before they lose patience")
    numCustomers = 0
    while numCustomers == 0:
        try:
            numCustomers = int(input("Number of customers that can wait in line: "))
        except:
            print("Invalid input")
    print("Let's play!")
    queue = Queue(numCustomers)
    firstRound = True
    playRound(queue,numCustomers,firstRound)
    print("There are no more customers in line")
    print("Thanks for playing")
main()
