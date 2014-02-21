# 6.00 Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#
# Name: Jimmy Bangun
# Collaborators: none
# 

import string
from graph import Digraph, Edge, Node

#
# Problem 2: Building up the Campus Map
#
# Each building of the Campus are set as nodes
# Path from building to adjacent building(s) represent edge(s)
# Total and Outdoor Distances represent weights of each edge
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    print "Loading map from file..."

    # Open File
    inFile = open(mapFilename, 'r', 0)

    # MIT: Digraph representing the MIT Map
    MIT = Digraph();
    
    # Generate list of map entries
    mapList = []
    for line in inFile:
        mapList.append(line.split())

    # Generate nodes
    nodes = []
    for entry in mapList:
        if entry[0] not in nodes:
            nodes.append(entry[0])
    for node in nodes:
        MIT.addNode(node)  

    # Generate edges
    edges = []
    for entry in mapList:
        singleEdge = Edge(entry[0], entry[1], int(entry[2]), int(entry[3]))
        edges.append(singleEdge)
    for edge in edges:
        MIT.addEdge(edge)

    # Print report    
    print "  ", len(nodes), "nodes loaded."
    print "  ", len(edges), "edges loaded."

    inFile.close()
    return MIT       

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# Objective is to find the Shortest Path using Brute Force Method by
# iterating through all possible paths and keeping track of the shortest path, 
# whilst satisfying the constraints of maximum Total Distance and Total Distance Outdoor
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    
    # Brute Force Outputs
    BFSResult = {}
    
    # Helper function to calculate Total Distance in a path
    def Dist(path):
        result = 0
        if path == None:
            return result
        if len(path) == 0:
            return result
        for i in range(len(path)-1):
            src = path[i]
            dest = path[i+1]
            for item in digraph.edges[src]:
                if item[0] == dest:
                    result += item[1]
        return result    
    
    # Helper function to calculate Total Outdoor Distance in a path
    def Out(path):
        result = 0
        if path == None:
            return result        
        if len(path) == 0:
            return result
        for i in range(len(path)-1):
            src = path[i]
            dest = path[i+1]
            for item in digraph.edges[src]:
                if item[0] == dest:
                    result += item[2]
        return result        

    # Helper function using DFS method
    def BFS(graph, start, end, maxD, maxO, path = [], result = None):
        path = path + [start]
        if start == end:
            return path
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles and constraints
                if result == None:
                    newPath = BFS(graph,node,end,maxD, maxO, path)
                    if newPath!= None and Dist(newPath) <= maxD and Out(newPath) <= maxO: 
                            result = newPath
                            distResult = Dist(result)
            if result != None and distResult not in BFSResult:
                BFSResult[distResult] = result
                if len(result) == 2 and result[-1] == end:
                    break
        

    BFS(digraph, start, end, maxTotalDist, maxDistOutdoors)
    if len(BFSResult) == 0:
        raise ValueError
    else:
        return BFSResult[min(BFSResult)]