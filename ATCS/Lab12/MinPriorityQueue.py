#Dylan Miller

#uses heaps to create a min-priority queue

from random import *

class MinPriorityQueue:
    """uses heaps to create a min-priority queue"""
    
    def __init__(self):
        """creates a heap and variable to track the working size"""
        self.heap = []
        self.heapSize = 0

    def size(self):
        """returns the working size of the heap"""
        return self.heapSize

    def getMin(self):
        """returns the minimum of the queue"""
        return self.heap[0]

    def extractMin(self):
        """returns and removes the minimum from the queue"""
        
        if self.heapSize < 1:
            return "heap underflow"

        #stores the minimum
        minimum = self.heap[0]
        #replaces the minimum with one of the last value
        self.heap[0] = self.heap[self.heapSize-1]
        #decreases the working size of the heap
        self.heapSize = self.heapSize-1
        #clears the value of the last index
        self.heap[self.heapSize] = None
        #calls heapify to reorder the heap
        self.heapify(0)
        
        return minimum

    def insert(self,x):
        """inserts a number into the queue"""

        #increases the working size of the heap
        self.heapSize = self.heapSize+1
        #adds a placeholder index
        self.heap.append(None)
        #adds a placeholder value
        self.heap[self.heapSize-1] = 99999

        if x > self.heap[self.heapSize-1]:
            return "new key is greater than current key"

        #sets the placeholder to the given value
        self.heap[self.heapSize-1] = x
        i = self.heapSize-1

        #while the current index is greater than one
        #and the parent is greater than the current value
        while i > 0 and self.heap[i//2] > self.heap[i]:
            #swap the parent and current
            self.heap[i],self.heap[i//2] = self.heap[i//2],self.heap[i]
            #set the new current to the parent
            i = i//2
            
    def heapify(self,index):
        """reorders the queue to maintain a min-heap"""

        #stores the index of the left and right child
        leftChild = (index*2)+1
        rightChild = (index*2)+2

        #finds the minimum of the current, left child, and right child
        if leftChild < self.heapSize and self.heap[leftChild] < self.heap[index]:
            minimum = leftChild
            
        else: minimum = index

        if rightChild < self.heapSize and self.heap[rightChild] < self.heap[minimum]:
            minimum = rightChild

        #if the current is not already the minimum
        if minimum != index:
            #swap the current and minimum
            self.heap[index],self.heap[minimum] = self.heap[minimum],self.heap[index]
            #recall heapify on the minimum
            self.heapify(minimum)

def kLargestValues(n,k):
    """finds the k largest values of a list n"""

    queue = MinPriorityQueue()
    for i in n:
        if queue.size() < k:
            queue.insert(i)
        else:
            #compares the current value with the min in the queue
            if queue.getMin() < i:
                queue.extractMin()
                queue.insert(i)
    return queue

def main():
    #min-priority queue
    queue = MinPriorityQueue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    
    queue.extractMin()
    queue.extractMin()
    
    queue.insert(1)
    queue.insert(5)
    queue.insert(6)
    queue.insert(7)
    
    queue.extractMin()
    queue.extractMin()
    
    queue.insert(8)

    print(queue.heap,queue.heapSize)

    #k largest values
    n = []
    for i in range(100):
        n.append(randint(0,100))
    k = 10
        
    print(kLargestValues(n,k).heap)
    
main()
