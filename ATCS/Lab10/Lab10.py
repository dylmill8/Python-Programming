#Dylan Miller

#implements edge, node, and network classes to represent a flow network
#and find the maximum flow from the source to the sink


class Node():
    "stores the label of a node and the edges in and out of it"

    def __init__(self,label):
        "creates two lists of in and out edges to the node"
        self.label = label
        self.inEdges = []
        self.outEdges = []

    def addInEdge(self,edge):
        "adds an edge object to the list of in edges"
        self.inEdges.append(edge)

    def addOutEdge(self,edge):
        "adds an edge object to the list of out edges"
        self.outEdges.append(edge)

    def getEdges(self):
        "returns both list of edges"
        return self.inEdges,self.outEdges

    def getLabel(self):
        "returns the string label of the node"
        return self.label

class Edge():
    "stores the start node, end node, flow, and capacity of an edge"

    def __init__(self,start,end,capacity):
        "sets start node, end node, and capacity variables and initializes flow to 0"
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0

    def setFlow(self,flow):
        "sets the flow value"
        self.flow = flow

    def getStart(self):
        "returns the start node"
        return self.start

    def getEnd(self):
        "returns the end node"
        return self.end

    def getCapacity(self):
        "reutrns the flow capacity"
        return self.capacity

    def getFlow(self):
        "returns the flow through the edge"
        return self.flow

class Network():
    "uses the edge and node classes to represent a flow network"
    
    def __init__(self):
        "creates a dictionary of node objects that is initialized with source and sink nodes and creates a list of edge objects"
        self.dictNodes = {}
        self.dictNodes["S"] = Node("S")
        self.dictNodes["T"] = Node("T")
        self.listEdges = []

    def add_node(self,label):
        "stores a node in the dictionary"
        self.dictNodes[label] = Node(label)

    def add_edge(self,a,b,c):
        "adds an edge from node a to node b with capacity c"
        a = self.dictNodes[a]
        b = self.dictNodes[b]
        edge = Edge(a,b,c)
        self.listEdges.append(Edge(a,b,c))
        a.addOutEdge(Edge(a,b,c))
        b.addInEdge(Edge(a,b,c))
        return edge

    def find_residual(self,current,visited,min_capacity):
        "finds and augments a path in the network, returning the residual"
        inEdges,outEdges = current.getEdges()
        visited.append(current)

        if current == self.dictNodes["T"]:
            return min_capacity

        #iterates through the in-edges of the current node
        for i in inEdges:
            capacity = i.getCapacity()
            flow = i.getFlow()
            
            #if the flow can be reduced and the start node is not visited
            if flow > 0 and i.getStart() not in visited:

                #recursively calls using the lower flow value as min_capacity
                if min_capacity < flow:
                    residual = self.find_residual(i.getStart(),visited,min_capacity)
                else: residual = self.find_residual(i.getStart(),visited,flow)

                #if the sink was found in the path
                if self.dictNodes["T"] in visited:
                    #try statement because residual is none if there are no existing paths
                    try:
                        #compares the residual at the stage of recursion with the min_capacity found at the end
                        if residual < min_capacity:
                            #stores the minimum value
                            min_capacity = residual
                    except: continue
                    
                    #sets the flow of the in-edge and out-edge between the start and end nodes
                    i.setFlow(flow - min_capacity)
                    start = i.getStart()
                    inEdges,outEdges = start.getEdges()
                    for j in outEdges:
                        if j.getEnd().getLabel() == i.getEnd().getLabel():
                            j.setFlow(flow - min_capacity)

                    return min_capacity
                
        #iterates through the out-edges of the current node
        for i in outEdges:
            capacity = i.getCapacity()
            flow = i.getFlow()

            #if the flow can be increased and the end node is not visited
            if capacity - flow > 0 and i.getEnd() not in visited:

                #recursively calls using the lower flow value as min_capacity
                if min_capacity < capacity - flow:
                    residual = self.find_residual(i.getEnd(),visited,min_capacity)
                else: residual = self.find_residual(i.getEnd(),visited,capacity - flow)

                #if the sink was found in the path
                if self.dictNodes["T"] in visited:
                    #try statement because residual is none if there are no existing paths
                    try:
                        #compares the residual at the stage of recursion with the min_capacity found at the end
                        if residual < min_capacity:
                            #stores the minimum value
                            min_capacity = residual
                    except: continue

                    #sets the flow of the in-edge and out-edge between the start and end nodes
                    i.setFlow(flow + min_capacity)
                    end = i.getEnd()
                    inEdges,outEdges = end.getEdges()
                    for j in inEdges:
                        if j.getStart().getLabel() == i.getStart().getLabel():
                            j.setFlow(flow + min_capacity)

                    return min_capacity

    def solve_network(self):
        "finds the maximum flow to the sink using find_residual()"
        while True:
            current = self.dictNodes["S"]
            visited = []
            min_capacity = 99999
            residual = self.find_residual(current,visited,min_capacity)

            #stops the loop when the sink is not reachable
            if self.dictNodes["T"] not in visited:
                break

        #calculates the maximum flow by summing the in-edges to the sink
        maxFlow = 0
        inEdges,outEdges = self.dictNodes["T"].getEdges()
        for i in inEdges:
            flow = i.getFlow()
            maxFlow = maxFlow + flow

##        prints the people and corresponding snacks/dollar amount for problem 2 & 3
##        nodes = self.dictNodes.values()
##        for i in nodes:
##            inEdges,outEdges = i.getEdges()
##            for j in outEdges:
##                print(j.getStart().getLabel(),j.getEnd().getLabel())
##                print(j.getFlow(),"/",j.getCapacity())
##                print()

        return maxFlow

def main():
    #problem 1
    network = Network()

    #test case from the class slides on max flow
    network.add_node("V1")
    network.add_node("V2")
    network.add_node("V3")
    network.add_node("V4")

    edge = network.add_edge("S","V1",16)
    edge = network.add_edge("S","V2",13)
    edge = network.add_edge("V1","V3",12)
    edge = network.add_edge("V2","V1",4)
    egde = network.add_edge("V2","V4",14)
    edge = network.add_edge("V3","V2",9)
    edge = network.add_edge("V3","T",20)
    edge = network.add_edge("V4","V3",7)
    egde = network.add_edge("V4","T",4)

    print("The max flow of the network is:",network.solve_network())

    #problem 2
    network = Network()

    #people nodes
    network.add_node("A")
    network.add_node("B")
    network.add_node("C")
    network.add_node("D")
    network.add_node("E")

    #snack nodes
    network.add_node("CM")
    network.add_node("KK")
    network.add_node("SN")
    network.add_node("P")
    network.add_node("RP")
    network.add_node("TM")

    #source to people
    edge = network.add_edge("S","A",1)
    edge = network.add_edge("S","B",1)
    edge = network.add_edge("S","C",1)
    edge = network.add_edge("S","D",1)
    edge = network.add_edge("S","E",1)

    #people to snacks
    edge = network.add_edge("A","TM",1)
    edge = network.add_edge("A","RP",1)

    edge = network.add_edge("B","SN",1)
    edge = network.add_edge("B","RP",1)
    edge = network.add_edge("B","KK",1)

    edge = network.add_edge("C","CM",1)
    edge = network.add_edge("C","P",1)
    edge = network.add_edge("C","SN",1)

    edge = network.add_edge("D","CM",1)

    edge = network.add_edge("E","CM",1)
    edge = network.add_edge("E","KK",1)
    edge = network.add_edge("E","SN",1)
    edge = network.add_edge("E","P",1)
    edge = network.add_edge("E","RP",1)
    edge = network.add_edge("E","TM",1)

    #snacks to sink
    edge = network.add_edge("CM","T",1)
    edge = network.add_edge("KK","T",1)
    edge = network.add_edge("SN","T",1)
    edge = network.add_edge("P","T",1)
    edge = network.add_edge("RP","T",1)
    edge = network.add_edge("TM","T",1)

    print("The max flow of the network is:",network.solve_network())

    #problem 3
    network = Network()

    #peopel nodes
    network.add_node("A")
    network.add_node("B")
    network.add_node("C")
    network.add_node("D")

    #source to net negative
    edge = network.add_edge("S","A",4)

    #people to people transactions
    edge = network.add_edge("A","B",2)
    edge = network.add_edge("A","C",2)

    edge = network.add_edge("B","D",1)
    edge = network.add_edge("B","T",1)

    edge = network.add_edge("C","T",2)

    edge = network.add_edge("D","T",1)

    print("The max flow of the network is:",network.solve_network())

main()
