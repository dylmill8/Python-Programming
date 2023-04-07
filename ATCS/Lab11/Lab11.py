#Dylan Miller

#given a graph represented by and adjacency list
#this function implements Prim's algorithmto finds the minimum spanning tree 

#finds minimum spanning tree given a graph as an adjacency list
def PrimMST(G):

    #holds the edges that comprise the minimum spanning tree
    MST = []
    #holds edges that have already been reached
    visited = [0]
    
    #while there are still unreached vertices
    while len(visited) < len(G):
        
        #holds the index of the end point of the minimum edge
        adjacentIndex = None
        #holds the start and end vertices of the minimum edge
        minimumEdge = None
        #holds the value of the current minimum edge
        minimumEdgeValue = 99999

        #iterates through all discovered vertices
        for i in visited:
            
            #iterates through adjacent edges
            for j in range(len(G[i])):
                
                #gets the lowest value edge that can be reached
                if 0 < G[i][j] < minimumEdgeValue and j not in visited:
                    minimumEdgeValue = G[i][j]
                    minimumEdge = (i,j)
                    adjacentIndex = j

        #adds the edge to the minimum spanning tree
        MST.append(minimumEdge)
        #adds the endpoint of the edge to the visited list
        visited.append(adjacentIndex)
    
    return MST

def main():
    #graph as an adjacency list
    G = [[0,7,0,5,0,0,0],
        [7,0,8,9,7,0,0],
        [0,8,0,0,5,0,0],
        [5,9,0,0,15,6,0],
        [0,7,5,15,0,8,9],
        [0,0,0,6,8,0,11],
        [0,0,0,0,9,11,0]]
    
    MST = PrimMST(G)
    #sums the weight of the edges in the minimum spanning tree
    MSTWeight = 0
    print ("Edge\tWeight")
    for i in MST:
        #prints the edge and weight (indexed from the original graph)
        print(i,"\t"+str(G[i[0]][i[1]]))
        MSTWeight = MSTWeight + G[i[0]][i[1]]
    print("MST weight:",MSTWeight)
main()
