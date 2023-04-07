# Name: Reilly Sheehan

from GraphAdjMatrix import GraphAdjMatrix
from Lab01Queue import Queue
import random

# returnSquares

class mine:
    "A mine is a graph that represents the board of Minesweeper."
    def __init__(self,size):
        """Creates a graph that contains 64 squares. Each square contains edges
with the squares it touches. Creates a list of numbers that represent the
distance to a mine: negative = mine, 1-8 = next to a mine, 0 = not next to a
mine."""
        self.size = size
        # Graph
        self.graph = GraphAdjMatrix()
        for i in range(self.size**2):
            # Add 3-8 edges to each vertex
            for j in self.getEdges(i):
                if not self.graph.isAdjacent(i,j):
                    self.graph.addEdge(i,j)
        self.numbers = []
        for i in range(self.size**2):
            # No mines yet, all are 0
            self.numbers.append(0)

    def generateMines(self,numMines,square):
        "Randomly generates mine locations, places them in graph and updates\
numbers for edges."
        self.mineLocs = []
        # Create list with all indexes
        options = []
        for i in range(self.size**2):
            options.append(i+1)
        # Remove square
        options.remove(square)
        # Remove square edges
        squareEdges = self.getEdges(square)
        for i in squareEdges:
            options.remove(i)
        # Generate random number for 10 mines
        for i in range(numMines):
            index = random.randrange(0,len(options))
            self.mineLocs.append(options[index])
            # Remove so a second mine can't be placed at that index
            options.remove(options[index])
        for i in self.mineLocs:
            #print(i,self.getEdges(i))
            # Set mine numbers to negative
            self.numbers[i-1] = -10
            # Add 1 to neighbors
            for j in self.getEdges(i):
                #print(i,j,self.numbers[63])
                self.numbers[j-1] += 1

    def returnNumber(self,x):
        return self.numbers[x-1]


    def clickedMine(self,square):
        "Returns true if the user square is a mine"
        if self.numbers[square-1] < 0:
                return True
        return False


    def returnSquares(self,x):
        colors = []
        for i in range(self.size**2):
            colors.append("white")
        colors[x-1] = "gray"
        queue = Queue(self.size**2/2)
        queue.enqueue(x)
        while queue.length() != 0:
            u = queue.dequeue()
            if self.numbers[u-1] == 0:
                for i in self.getEdges(u):
                    if colors[i-1] == "white":
                        colors[i-1] = "gray"
                        queue.enqueue(i)
            colors[u-1] = "black"
        squares = []
        for i in range(len(colors)):
            if colors[i] == "black":
                squares.append(i+1)
        return squares
        
                


    def getEdges(self,x):
        "Helper function to get edges"
        # Start off with all 8 edges available
        edges = [(x-(self.size+1)),(x-(self.size)),(x-(self.size-1)),(x-1),\
                 (x+1),(x+(self.size-1)),(x+(self.size)),(x+(self.size+1))]
        # Number is on top row; remove edges above
        if x-self.size < 1:
            edges.remove(x-(self.size+1))
            edges.remove(x-(self.size))
            edges.remove(x-(self.size-1))
        # Number is on bottom row; remove edges below
        if x+self.size > self.size**2:
            edges.remove(x+(self.size-1))
            edges.remove(x+(self.size))
            edges.remove(x+(self.size+1))
        # Number is on right side; remove edges to right
        if x%self.size == 0:
            if (x-(self.size-1)) in edges:
                edges.remove(x-(self.size-1))
            edges.remove(x+1)
            if (x+(self.size+1)) in edges:
                edges.remove(x+(self.size+1))
        # Number is on left side; remove edges to left
        if (x-1)%self.size == 0:
            if (x-(self.size+1)) in edges:
                edges.remove(x-(self.size+1))
            edges.remove(x-1)
            if (x+(self.size-1)) in edges:
                edges.remove(x+(self.size-1))
        # Return list of edges
        return edges



##def main():
##    x= mine(8)
##    print(x.getEdges(14))
##    print(x.getEdges(64))
##    x.generateMines(10,14)
##    print(x.mineLocs)
##    print(x.numbers)
##main()
