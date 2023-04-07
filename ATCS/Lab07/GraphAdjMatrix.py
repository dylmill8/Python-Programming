#Dylan Miller

#implements a graph using an adjacency Matrix comprised of subarrays

#creates an adjacency matrix of subarrays
class GraphAdjMatrix:
    """creates an adjacency matrix of subarrays"""
    def __init__(self):
        #adjMatrix tracks the edges
        #indices tracks the vertices
        self.adjMatrix = []
        self.indices = []

    #gets the index of vertex x in the adjMatrix
    def getIndex(self,x):
        """gets the index of vertex x in the adjMatrix"""
        for i in range(len(self.indices)):
            if self.indices[i] == x:
                return i
        return False

    #adds a new edge between vertices u and v
    def addEdge(self,u,v):
        """adds a new edge between vertices u and v"""
        #if u and v already have an edge between them then return
        if self.isAdjacent(u,v) == True:
            return
        #grabs the index position of u and v in the adjMatrix
        uIndex = self.getIndex(u)
        vIndex = self.getIndex(v)
        #if u is not an existing vertex
        if uIndex is False:
            newVertex = []
            #appends 0 to the lists of all existing vertices and
            #creates a list of 0's for the new vertex u
            for i in range(len(self.indices)):
                newVertex.append(0)
                self.adjMatrix[i].append(0)
            #appends 0 an extra time to include itself
            newVertex.append(0)
            #adds the list of connections for the new vertex to the adjMatrix
            self.adjMatrix.append(newVertex)
            #adds u to the list of indices
            self.indices.append(u)
        #repeats for vertex v
        if vIndex is False:
            newVertex = []
            for i in range(len(self.indices)):
                newVertex.append(0)
                self.adjMatrix[i].append(0)
            newVertex.append(0)
            self.adjMatrix.append(newVertex)
            self.indices.append(v)
        #create an edge by taking new index positions and changing a 0 to 1
        uIndex = self.getIndex(u)
        vIndex = self.getIndex(v)
        self.adjMatrix[uIndex][vIndex] = 1
        self.adjMatrix[vIndex][uIndex] = 1

    #deletes the edge between vertices u and v
    def deleteEdge(self,u,v):
        """deletes the edge between vertices u and v"""
        uIndex = self.getIndex(u)
        vIndex = self.getIndex(v)
        #if both u and v exist in the matrix
        if uIndex is not False and vIndex is not False:
            #set the edges to 0
            self.adjMatrix[uIndex][vIndex] = 0
            self.adjMatrix[vIndex][uIndex] = 0
            
    #gets a list of all vertices that share an edge with vertex u
    def getNeighbors(self,u):
        """gets a list of all vertices that share an edge with vertex u"""
        uIndex = self.getIndex(u)
        neighbors = []
        for i in range(len(self.adjMatrix[uIndex])):
            #if there is a connection between u and another vertex
            if self.adjMatrix[uIndex][i] > 0:
                #append the other vertex to the list of neighbors
                neighbors.append(self.indices[i])
        return neighbors
        
    #returns True if vertices u and v are neighbors
    def isAdjacent(self,u,v):
        """returns True if vertices u and v are neighbors"""
        uIndex = self.getIndex(u)
        vIndex = self.getIndex(v)
        if uIndex or vIndex is False:
            return False
        if len(self.indices) == 0:
            return False
        #if there is an edge between u return True
        if self.adjMatrix[uIndex][vIndex] > 0:
            return True
        else: return False

    #prints the adjacency matrix by rows and columns
    def __str__(self):
        stringMatrix = ""
        for i in self.adjMatrix:
            element = i
            stringMatrix = stringMatrix+"".join(str(element))+"\n"
        return "indices: "+str(self.indices)+"\n"+stringMatrix

def main():
    adjMatrix = GraphAdjMatrix()
    adjMatrix.addEdge(1,2)
    adjMatrix.addEdge(1,2)
    adjMatrix.addEdge(1,2)
    adjMatrix.addEdge(1,3)
    adjMatrix.addEdge(1,4)
    adjMatrix.addEdge(2,5)
    adjMatrix.addEdge(2,6)
    adjMatrix.addEdge(5,6)
    print(adjMatrix.getNeighbors(1))
    print(adjMatrix.isAdjacent(1,6))
    print(adjMatrix.isAdjacent(1,4))
    adjMatrix.deleteEdge(1,7)
    adjMatrix.deleteEdge(1,3)
    adjMatrix.deleteEdge(1,3)
    print(adjMatrix.getNeighbors(1))
    print(adjMatrix.getNeighbors(3))
    print(adjMatrix)
main()
