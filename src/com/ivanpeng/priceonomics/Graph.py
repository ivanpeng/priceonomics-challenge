'''

The basic graph class for holding data structure.
Created on 2013-10-29

@author: Ivan
'''
from numpy import matrix
from numpy import linalg
from numpy import zeros

class Node():
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
class Edge():
    def __init__(self, startNode=None, endNode=None, value=None):
        self.startNode = startNode
        self.endNode = endNode
        self.value = value
        
    def __str__(self):
        return "Start from Node " + str(self.startNode) + " to " + str(self.endNode) + " with value " + str(self.value)
    
    def __repr__(self):
        return "Start from Node " + str(self.startNode) + " to " + str(self.endNode) + " with value " + str(self.value)

class Graph():
    def __init__(self, numNodes=0, numEdges=0):
        self.numNodes = numNodes
        self.nodes = {}
        if (numEdges == 0 and numNodes != 0):
            # number of edges will be n^2-n
            self.numEdges = numNodes**2 - numNodes
        else:
            self.numEdges = numEdges
        self.edges = []
    
    def addEdge(self, start, end, value):
        # start and end are strings, not indexes
        if (start not in self.nodes):
            self.nodes[start] = Node(start)
        if (end not in self.nodes):
            self.nodes[end] = Node(end)
        self.edges.append(Edge(start, end, value))
        
    def getEdge(self, start, end):
        for itr,val in enumerate(self.edges):
            if (val.startNode == start and val.endNode == end):
                return val 
        return None
        
    def toAdjacencyMatrix(self):
        self.adjMatrix = zeros(shape=(self.numNodes, self.numNodes))
        for i,vali in enumerate(self.nodes):
            for j, valj in enumerate(self.nodes):
                if (i != j):
                    self.adjMatrix[i,j] = self.getEdge(vali, valj).value
        print self.adjMatrix
        # no need to return this, as this is just saved.
    
    def spectralAnalysis(self):
        # Assumes adjacency matrix is already made
        for i in range(2,self.numNodes+1):
            m = linalg.matrix_power(self.adjMatrix,i)/i
        print "Spectral analysis, k= " + str(i) + ":\n" + str(m)
        print ""
        return m.diagonal()
    
    def __str__(self):
        return "Nodes: " + str(self.nodes) + "\nEdges: " + str(self.edges)
    
    def __repr(self):
        return "Nodes: " + self.nodes + "\nEdges: " + self.edges