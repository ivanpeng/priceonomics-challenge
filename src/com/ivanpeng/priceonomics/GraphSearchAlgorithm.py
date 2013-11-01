'''
This is the template for graph searching for the Arbitrage loop problem. 
In the graph traversal, loops of two may be accepted. 
Created on 2013-10-29

@author: Ivan

'''

'''
This is a modified depth-first search class. Instead of a goal node, the final node is itself. However, having the arbitrage loop being
an (almost) complete graph, we have to accommodate for loops of different lengths. We will find all loops of 2, 3, and 4, and then compare
the paths. 
This is the second interation of the Greedy algorithm. The third iteration will be a DFSModified with a Heuristic.
'''
class DFSModified():
    def __init__(self, graph):
        self.graph = graph
        self.path = []
        self.edgeList = []
        
    def determineExchange(self):
        scores = []
        for p in self.path:
            score = 1
            for itr,val in enumerate(p[:-1]):
                score *= self.graph.getEdge(p[itr], p[itr+1]).value
            scores.append(score)
        index = scores.index(max(scores))
        print "Max score is " + str(max(scores)) + " with the path being " + str(self.path[index])
        return self.path[index]
    
    def traverse(self, currentNode, traversedPath=[] ):
        # follow standard dfs algorithm; only thing that changes is the exit
        if (len(traversedPath) == 0):
            traversedPath.append(currentNode)
            # need to call traverse here, but extra 
            traversedPath = self.traverse(currentNode, traversedPath)
        elif (currentNode == traversedPath[0] and len(traversedPath) > 1):
            # we have hit a full loop; assign this path to the path list and exit
            self.path.append(traversedPath)
            return traversedPath[:-1]
        else:
            nodeList = [a for a in self.graph.nodes if a != currentNode and a not in traversedPath[1:]]
            # score list of nodes outbound
            for node in nodeList:
                # know this nodeList is already of ones not explored, so we can just jump to traversal
                traversedPath.append(node)
                traversedPath = self.traverse(node, traversedPath)
            return traversedPath[:-1]

'''
This is the class which will do the graph traversal. Utilizing a heuristic which simply is the max of the ratio in outgoing edges, we will
calculate what the best path is, from 
'''
class GreedyNoRepeat():
    def __init__(self, graph, length=3):
        self.graph = graph
        self.path = []
        self.exchangeList = []
        self.length = length
        self.heuristic = BasicHeuristic(graph)
    
    def traverse(self, currentNode, k=0):
        # This is a recursive algorithm
        # more than one case to check for
        # if first node
        if (len(self.path) == 0):
            # first case; append current node
            self.path.append(currentNode)
            self.traverse(currentNode, k+1)
        
        elif (currentNode == self.path[0] and len(self.path) > 1):
            # we have hit a full loop; exit
            return self.path
        else:
            # otherwise, continue as planned.
            # gather list of nodes outgoing 
            nodeList = [a for a in self.graph.nodes if a != currentNode and a not in self.path[1:]]
            print "List of nodes: " + str(nodeList)
            # score list of nodes outbound
            scores = []
            for node in nodeList:
                scores.append(self.heuristic.scoreRatio(currentNode, node))
            # choose max of list, and then go in that direction
            index = scores.index(max(scores))
            # append node to path, and call traverse with k incremented
            # need extra check case if it's first case
            self.path.append(nodeList[index])
            # Track edge values as well
            edge = self.graph.getEdge(currentNode, nodeList[index])
            self.exchangeList.append(edge.value)
            # recursive call!
            self.traverse(nodeList[index], k+1)
        return self.path
        
class BasicHeuristic():
    def __init__(self, graph):
        self.graph = graph
    
    def scoreRatio(self, startNode, endNode):
        edgeAway = self.graph.getEdge(startNode, endNode)
        edgeTo = self.graph.getEdge(endNode, startNode)
        return edgeAway.value*edgeTo.value
        