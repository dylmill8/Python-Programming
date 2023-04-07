#Dylan Miller

#implements a graph using an adjacency list comprised of linked lists

#import doubly linked list class
from Lab01DLLArray import *

#creates an adjacency list of linked lists
class GraphAdjList:
    """creates an adjacency list of linked lists"""
    #indices list tracks the vertex nodes
    #adjList tracks the edges/neighbors at a vertex
    def __init__(self):
        self.adjList = []
        self.indices = []
        
    #adds a new egde connection between two vertices
    def addEdge(self,u,v):
        """adds an edge between vertices u and v"""
        #if u and v are already connected then return
        if self.isAdjacent(u,v) == True:
            return
        #tracks if the u or v are new vertex nodes
        newU,newV = True,True
        #iterate through the list of known indices
        for i in range(len(self.indices)):
            #if u is a known vertex
            if self.indices[i] == u:
                #inserts v into linked list u
                self.adjList[i].insert(v)
                newU = False
            #if v is a known vertex
            if self.indices[i] == v:
                #inserts u into linked list v
                self.adjList[i].insert(u)
                newV = False
        #if there is a new vertex node add the node to the list of vertices
        #and its neighbor to the adjacency list
        if newU == True:
            linkedList = DLLArray()
            self.adjList.append(linkedList)
            self.adjList[-1].insert(v)
            self.indices.append(u)
        if newV == True:
            linkedList = DLLArray()
            self.adjList.append(linkedList)
            self.adjList[-1].insert(u)
            self.indices.append(v)

    #deletes an edge between two vertices
    def deleteEdge(self,u,v):
        """deletes an edge from vertices u and v"""
        for i in range(len(self.indices)):
            #if u is in the list of vertices delete v from its linked list
            if self.indices[i] == u and self.isAdjacent(u,v) == True:
                self.adjList[i].delete(v)
            #if v is in the list of vertices delete u from its linked list
            if self.indices[i] == v and self.isAdjacent(v,u) == True:
                self.adjList[i].delete(u)

    #returns the linked list of the given vertex
    def getNeighbors(self,u):
        """returns the linked list of neighbors of the vertex u"""
        for i in range(len(self.indices)):
            #if u is in the list of vertices
            if self.indices[i] == u:
                #returns a list of the values in the linked list for vertex u
                return self.adjList[i].getValues()

    #returns whether or not two vertices are neighbors
    def isAdjacent(self,u,v):
        """returns True if vertices u and v are neighbors"""
        #if there are no vertices then return false
        if len(self.indices) == 0:
            return False
        for i in range(len(self.indices)):
            #if u is in the list of known vertices
            if self.indices[i] == u:
                #get all of its neighbors from the linked list
                neighbors = self.adjList[i].getValues()
        #if v is in the list of neighbors return True
        if v in neighbors:
            return True
        else: return False

def main():
    adjList = GraphAdjList()
    adjList.addEdge(1,2)
    adjList.addEdge(1,2)
    adjList.addEdge(1,2)
    adjList.addEdge(1,3)
    adjList.addEdge(1,4)
    adjList.addEdge(2,5)
    adjList.addEdge(2,6)
    print(adjList.getNeighbors(1))
    print(adjList.isAdjacent(1,6))
    print(adjList.isAdjacent(1,4))
    adjList.deleteEdge(1,3)
    adjList.deleteEdge(1,3)
    adjList.deleteEdge(1,7)
    print(adjList.getNeighbors(1))
    print(adjList.getNeighbors(3))
main()
