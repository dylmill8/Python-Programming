
# Name: Reilly Sheehan

# This module will contain the GraphAdjMatrix which greates a graph using an
# adjacency matrix representation.

class GraphAdjMatrix:
    """A GraphAdjList contains a representation of the vertices and edges that
make up a graph."""
    
    def __init__(self):
        "Creates empty dictionary and graph"
        # Dictionary: vertices are keys, values are vertices' indexes in graph
        self.vertices = {}
        # Graph is list of lists, each value represents edge
        self.graph = []

    def addEdge(self,u,v):
        "Adds edge between u and v; creates vertices if they do not yet exist."
        # Create vertices if they don't exist
        if u not in self.vertices:
            self.createVertex(u)
        if v not in self.vertices:
            self.createVertex(v)
        # Add one to each value in the graph
        self.graph[self.vertices[u]][self.vertices[v]] = 1
        #self.graph[self.vertices[v]][self.vertices[u]] += 1
        

    def deleteEdge(self,u,v):
        "Deletes edge between u and v."
        try:
            # Subtract 1 from graph value if an edge exists
            if self.graph[self.vertices[u]][self.vertices[v]] > 0:
                self.graph[self.vertices[u]][self.vertices[v]] = 0
                #self.graph[self.vertices[v]][self.vertices[u]] -= 1
            else:
                print("Edge does not exist.")
        except:
            print("Edge does not exist.")


    def getNeighbors(self,u):
        "Returns list of edges of u."
        try:
            # Create list to add edges to
            x = []
            # Loop through u's list in self.graph
            for i in range(len(self.graph[self.vertices[u]])):
                vert = None
                # Loop through vertices dictionary to find vertex
                for j in list(self.vertices.items()):
                    if j[1] == i:
                        vert = j[0]
                # Add vertex to x for how many edges it shares
                for k in range(self.graph[self.vertices[u]][i]):
                    x.append(vert)
            return x
        except:
            return
            #print("Vertex does not exist.")


    def isAdjacent(self,u,v):
        "Returns True if u and v share an edge; False if not."
        x = self.getNeighbors(u)
        if x != None:
            for i in x:
                if i == v:
                    return True
            return False


    def createVertex(self,x):
        "Helper function to create a vertex"
        # Key = x, value = graph index
        self.vertices[x] = len(self.graph)
        # Add extra spot to each list
        for i in self.graph:
            i.append(0)
        # Add new list to graph
        self.graph.append([])
        # Add empty spots to fill out graph
        for i in range(len(self.graph)):
            self.graph[self.vertices[x]].append(0)

    def printGraph(self):
        "Helper function that prints graph"
        y = "   "
        for i in range(len(self.graph)):
            x = list(self.vertices.items())
            print(self.graph[i])
            #print(x[i][0],self.graph[i])
            #y += str(x[i][0])+"  "
        #print(y)

        #print(self.vertices,self.graph)

    #Dylan
    def getAdjacent(self,u,v):
        "returns a list of the same sign adjacent neighbors (odd/even)"
        adjacent = []
        #checks where the current square is in the boundary and
        #appends the neighbors to the list
        if v <= (len(self.vertices)-3):
            adjacent.append((u,v+2))
        if v >= 2:
            adjacent.append((u,v-2))
        if u >= 2:
            adjacent.append((u-2,v))
        if u <= (len(self.vertices)-3):
            adjacent.append((u+2,v))
        return adjacent
        

## TESTING ##
##def main():
##    x=GraphAdjMatrix()
##    x.addEdge(1,2)
##    x.addEdge(2,3)
##    x.addEdge(3,5)
##    x.addEdge(2,9)
##    x.addEdge(1,4)
##    x.addEdge(2,1)
##    x.printGraph()
##    x.deleteEdge(3,5)
##    x.printGraph()
##    x.deleteEdge(3,3)
##    print(x.getNeighbors(2))
##    print(x.getNeighbors(8))
##    print(x.isAdjacent(9,2))
##    print(x.isAdjacent(8,2))
##
##main()
