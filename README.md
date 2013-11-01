priceonomics-challenge
======================

A modified DFS algorithm to solve the Priceonomics Puzzle.

This project is solving the following problem: http://priceonomics.com/jobs/puzzle/

It is developed in python, namely pydev. To run, clone the project, and run it through pydev. Or, to run through python shell, open up a terminal/command prompt, cd to the folder, and run:

$ python DataInput.py

The results should be outputted in fashion.

Algorithm:

There are two algorithms being tried here. The first is a DFS (depth-first search) algorithm, brute forcing all possible cycles/loops of the (almost) complete exchange graph, and then determining the score on each of them. This is obviously an NP-complete problem, as it has shades of the Travelling Salesman, so we resort to a Greedy type algorithm to determine the next best case. 

The modified DFS is a recursive algorithm, essentially searching if the current node is the starting node. If it is, then it records the path, and then backtracks out before traversing again.

There is an interesting mathematical property that can be found with setting up the Arbitrage Loop problem. With the graph, we create an adjacency matrix (definition here: http://en.wikipedia.org/wiki/Adjacency_matrix). However, being a directed and weighted graph, this is going to be asymmetrical and not all 1s and 0s. However, we may utilize spectral analysis. For spectral theory, if we take the matrix power k of the adjacency matrix A, A^k, the (i,j)th element describes the number of ways to get from node i to node j. While not useful, if we take 1/k*A^k, it may be interpreted as the average of exchange ratios going from node i to j. Since we are looking at cycles, we only have to consider the diagonal of the matrix.

Looking at the diagonals and seeing what is the max allows us to select the starting node, which is another problem. Although not proven rigorously, test runs on evidence certainly seem to prove that the elements along diagonal with the highest spectral number roughly equate to the starting node having the best ratio.

The greedy algorithm has yet to been tested in collaboration.

Assumptions:

One of the biggest assumptions I'm making is that aside from the starting node, all other nodes can only be visited once. This was a restriction on the length of loop, but will be extended in future versions.
