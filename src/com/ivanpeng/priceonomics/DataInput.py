'''
Basic template for loading data. Will call Priceonomics API, and return a graph object. Uses JSON parser.
Created on 2013-10-29

@author: Ivan
'''


import json
import urllib2
import math
from time import gmtime, strftime
from Graph import Graph
from GraphSearchAlgorithm import *

#url = "http://fx.priceonomics.com/v1/rates/"
#data = json.load(urllib2.urlopen(url))
# write data to file
#filename = 'arbitrage_data_' + strftime("%Y-%m-%d-%H-%M-%S",gmtime()) + ".txt"
#with open(filename, 'wb') as outfile:
#    json.dump(data, outfile)
with open('arbitrage_data_2013-10-30-05-04-21.txt', 'r') as infile:
    data = json.load(infile)
graphObj = Graph(int(math.sqrt(len(data))))
for itr,elem in enumerate(data):
    currencies = elem.split("_")
    if (currencies[0] != currencies[1]):
        # add to graph element
        # Graph addEdge needs to take care of nodes as well.
        graphObj.addEdge(currencies[0], currencies[1], float(data[elem]))
    print elem + ":" +data[elem]
print graphObj
graphObj.toAdjacencyMatrix()
graphObj.spectralAnalysis()

for i, node in enumerate(graphObj.nodes):
    print "Traversal from node " + str(node)
    gdfs = DFSModified(graphObj)
    gdfs.traverse(node, [])
    print str(gdfs.path)
    gdfs.determineExchange()

'''
# now that we have the graphing object, proceed to determine the traversal loop
for i,node in enumerate(graphObj.nodes):
    #GreedyNoRepeat(graphObj, 2).traverse(node)
    print "Traversal from node " + str(node) + " with 3 length as minimum"
    g3 = GreedyNoRepeat(graphObj, 3)
    g3.traverse(node)
    print "From traversal, the optimal path is " + str(g3.path) + "\n\n"
'''

