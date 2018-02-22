class vertex:
    def __init__(self,connectedTo=None,weight=None):
        self.connectedDict = {}
        self.connectedDict[connectedTo] = weight
    def __str__(self):
        return str(self.connectedDict)

class graph:
    def __init__(self):
        self.graphDict = {}



    def addEdge(self,firstVertex,secondVertex,weight):
        if firstVertex and secondVertex in self.graphDict:
            self.graphDict[firstVertex].connectedDict[secondVertex] = weight
        else:
            return "No Vertex"

    def addVertex(self,vertex1):
        if vertex1 in self.graphDict:
            return "already added"
        else:
            self.graphDict[vertex1]=vertex()

    def getEdge(self,vertex):
        return self.graphDict[vertex]


    def __str__(self):
        return str(self.graphDict)


g = graph()


for i in range(1,5):
    g.addVertex(i)

g.addEdge(1,2,4)
g.addEdge(1,3,5)
g.addEdge(3,4,7)
g.addEdge(2,4,6)
g.addEdge(3,2,9)

print g.getEdge(3).connectedDict[2]