'''
Basic template for loading data. Will call Priceonomics API, and return a graph object. Uses JSON parser.
Created on 2013-10-29

@author: Ivan
'''


import json
import urllib2
import math
from time import gmtime, strftime, time
from Graph import Graph
from GraphSearchAlgorithm import *

url = "http://fx.priceonomics.com/v1/rates/"
data = json.load(urllib2.urlopen(url))
# write data to file
#filename = 'arbitrage_data_' + strftime("%Y-%m-%d-%H-%M-%S",gmtime()) + ".txt"
#with open(filename, 'wb') as outfile:
#    json.dump(data, outfile)
#with open('arbitrage_data_2013-10-30-05-04-21.txt', 'r') as infile:
#    data = json.load(infile)
graphObj = Graph(int(math.sqrt(len(data))))
for itr,elem in enumerate(data):
    currencies = elem.split("_")
    if (currencies[0] != currencies[1]):
        # add to graph element
        # Graph addEdge needs to take care of nodes as well.
        graphObj.addEdge(currencies[0], currencies[1], float(data[elem]))
    #print elem + ":" +data[elem]
print graphObj
graphObj.toAdjacencyMatrix()
diagonal = graphObj.spectralAnalysis()
diagonal = list(diagonal)
ind = diagonal.index(max(diagonal))
print "Spectral analysis yields node with index " + str(ind) + " as most potential to have the greatest profit for arbitrage"
#TODO: implement ordered dictionary

if (len(graphObj.nodes) > 10):
    print "Using greedy algorithm"
else:
    print "Using brute-force DFS algorithm"
for i, node in enumerate(graphObj.nodes):
    print "Starting at node " + str(node)
    if (len(graphObj.nodes) > 10):
        g3 = GreedyNoRepeat(graphObj)
        g3.traverse(node)
        print "From traversal, the optimal path is " + str(g3.path) + "\n\n"
    else:
        startTime = time()
        gdfs = DFSModified(graphObj)
        gdfs.traverse(node, [])
        print "From traversal, the set of all paths is " + str(gdfs.path) + "\n\n"
        gdfs.determineExchange()
        print "Total time of computation was " + str(time() - startTime)

print "==========================================="
print "Greedy Algorithm"

# now that we have the graphing object, proceed to determine the traversal loop
for i,node in enumerate(graphObj.nodes):
    print "Traversal from node " + str(node) 
    startTime = time()
    g3 = GreedyNoRepeat(graphObj, 3)
    g3.traverse(node)
    print "From traversal, the optimal path is " + str(g3.path) + "\n\n"
    print "Total time of computation was " + str(time()-startTime)


