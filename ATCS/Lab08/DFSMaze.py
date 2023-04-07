#Dylan Miller

#this program implements Depth First Search on a graoh to create a Maze
#where 1's represent walls and 0's are pathways

from GraphAdjMatrix import *
from random import *

class Maze:
    "stores a maze using an adjacency matrix graph"
    def __init__(self):
        "creates matrix and empty lists to store visited rooms and marked corridors"
        self.graph = GraphAdjMatrix()
        self.visited = []
        self.marked = []

    def generateMaze(self,N,M):
        "creates a graph N x M to represent the maze"
        #creates vertices for N x M
        for i in range((2*N)+1):
            self.graph.createVertex(i)
            
        #creates walls along the border
        for i in range((2*N)+1):
            self.graph.addEdge(0,i)
            self.graph.addEdge(2*N,i)
            self.graph.addEdge(i,2*N)
            self.graph.addEdge(i,0)

            #adds all the border walls to list of visited squares
            self.visited.append((0,i))
            self.visited.append((2*N,i))
            self.visited.append((i,2*N))
            self.visited.append((i,0))
  
        #itterates through all squares of the maze
        for i in range(((2*N)+1)*((2*M)+1)):
            #takes only odd rows and columns
            if (i%((2*N)+1))%2 == 1 and (i//((2*M)+1))%2 == 1:
                #sets the row and column
                row = i%((2*N)+1)
                column = i//((2*M)+1)
                #calls DFS on every odd row & column (room)
                self.DFS(row,column)

        #reiterates through the maze
        for i in range(((2*N)+1)*((2*M)+1)):
            row = i%((2*N)+1)
            column = i//((2*M)+1)
            #if a square was not visited by DFS (islands) then place a wall
            if (row,column) not in (self.visited+self.marked):
                self.graph.addEdge(row,column)
        
        return self.graph

    def DFS(self,u,v):
        "performs Depth First Search on sqaure (u,v) where u is the row and v is the column"
        #if the room is unvisited
        if (u,v) not in self.visited:
            #add the current room to the visited list
            self.visited.append((u,v))

            #get the odd adjacent squares
            adjacentSquares = self.graph.getAdjacent(u,v)
            #randomize the order
            shuffle(adjacentSquares)

            #for each adjacent square (neighbor)
            for i in adjacentSquares:
                #set the indices of the neighbor sqaure to variables
                u1,v1 = i[0],i[1]

                #u,v is current
                #u1,v1 is neighbor
                #u2,v2 is corridor
                
                #finds the indices of the corridor betweeen the neighbor and current
                u2,v2 = u,v
                if u1 > u:
                    u2 = u+1
                elif u1 < u:
                    u2 = u-1
                elif v1 > v:
                    v2 = v+1
                elif v1 < v:
                    v2 = v-1

                #if the neighbor is unvisited
                if (u1,v1) not in self.visited:
                    #marks the corridor (already set to walkable)
                    self.marked.append((u2,v2))
                    #recurse on neighbor
                    self.DFS(u1,v1)

                #if the corridor wasn't marked
                elif (u2,v2) not in self.marked:
                    #add an edge to the graph (wall)
                    self.graph.addEdge(u2,v2)
                    #mark corridor
                    self.marked.append((u2,v2))
        else:
            return
    
    def printMaze(self):
        "prints the graph of the maze"
        self.graph.printGraph()

##def main():
##    N = 13
##    M = 13
##    maze = Maze()
##    maze.generateMaze(N,M)
##    maze.printMaze()
##
##main()
