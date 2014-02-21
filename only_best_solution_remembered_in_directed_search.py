# 6.00 Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#
# Name:
# Collaborators:
#

import string
from graph import Edge, WeightedDigraph
from decorators import timing

LARGE_DIST = 1000000

def total_distances(graph, path, total=None, outdoors=None):
    """ Find total distance traveled and outdoors traveled,
        if it is less than total and outdoors parameters (if those are given)
    """
    distances = [(0, 0)]
    for this, after in zip(path, path[1:]):
        w = graph.weights[this, after]
        new_distances = []
        for edge in w:
            #print this, edge, after
            this_total, this_outdoors = edge
            new_distances.extend(
                [(tot + this_total, ins + this_outdoors)
                    for tot, ins in distances
                    if (total is None or tot + this_total <= total) and
                        (outdoors is None or ins + this_outdoors <= outdoors)])
        distances = new_distances
    return distances
#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph
#
@timing
def load_map(mapFilename):
    """
    _parses the map file and constructs a directed graph

    _parameters:
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
    # TODO
    print "Loading map from file..."
    campus = WeightedDigraph()
    with open(mapFilename) as infile:
        for line in infile:
            data = line.split()
            for d in data[:2]:
                try:
                    campus.addNode(d)
                except ValueError:
                    pass
            campus.addEdge(Edge(data[0], data[1]))
            campus.addWeights(data[0], data[1], map(int, data[2:]))
    return campus

#
# Problem 3: Finding the Shortest _path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#
@timing
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.
    Repeatedly calculates the path distances by total_distances.

    _parameters:
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
    if maxTotalDist < 0 or maxDistOutdoors < 0:
        raise ValueError('Distance limit unsatisfyable!')
    elif start == end:
        return []
    new_path = [[start]]
    path = None
    solutions = []
    path_cost = [0, 0]
    while new_path:
        path = new_path
        new_path = [p + [child] for p in path
                    for child in digraph.childrenOf(p[-1])
                    if child not in p and p[-1] != end]
        new_solutions = [(total_distances(digraph, p, maxTotalDist, maxDistOutdoors), p)
                         for p in new_path if p[-1] == end]
        if new_path:
            solutions.extend([sol for sol in new_solutions if sol[0]])
            print len(solutions),
    print
    if not solutions:
        raise ValueError('No such path!')
    return min(solutions)[1]

#
# Problem 4: Finding the Shorest _path using Optimized Search Method
#
@timing
def directedBFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.
    Calculates the path distances by extending the old distances from previous paths.

    _parameters:
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
    if maxTotalDist < 0 or maxDistOutdoors < 0:
        raise ValueError('Distance limit unsatisfyable!')
    elif start == end:
        return []
    new_path = [[(0, 0), [start]]]
    path = None
    m = ((float('inf'), float('inf')), [])
    while new_path:
        path = new_path
        new_path = [((total + total_child, outdoors + outdoors_child), p + [child])
                        for (total, outdoors), p in path
                        for child in digraph.childrenOf(p[-1])
                        for total_child, outdoors_child in digraph.weights[p[-1], child]
                        if child not in p and child != end and
                        (total + total_child <= maxTotalDist and
                         outdoors + outdoors_child <= maxDistOutdoors)]
        solution = [((total + total_child, outdoors + outdoors_child), p + [child])
                          for (total, outdoors), p in path
                            for child in digraph.childrenOf(p[-1])
                            for total_child, outdoors_child  in digraph.weights[p[-1], child]
                            if child == end and (total + total_child <= maxTotalDist and
                                                 outdoors + outdoors_child <= maxDistOutdoors)]
        #print len(solutions),
        if solution:
            solution = min(solution)
            if m[0][0] > solution[0][0]:
                m = solution
                maxTotalDist = m[0][0] - 1
    if m[1]:
        return m[1]
    else:
        raise ValueError('No such path!')

# Uncomment below when ready to test
if __name__ == '__main__':
##    # Test cases
    digraph = load_map("mit_map.txt")
    print digraph


    # Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expected_path1 = ['32', '56']
    brute_path1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    bfs_path1 = directedBFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expected_path1
    print "Brute-force: ", brute_path1
    print "BFS: ", bfs_path1
    
    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expected_path2 = ['32', '36', '26', '16', '56']
    brute_path2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
    bfs_path2 = directedBFS(digraph, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expected_path2
    print "Brute-force: ", brute_path2
    print "BFS: ", bfs_path2

    # Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expected_path3 = ['2', '3', '7', '9']
    brute_path3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    bfs_path3 = directedBFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expected_path3
    print "Brute-force: ", brute_path3
    print "BFS: ", bfs_path3

    # Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expected_path4 = ['2', '4', '10', '13', '9']
    brute_path4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
    bfs_path4 = directedBFS(digraph, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expected_path4
    print "Brute-force: ", brute_path4
    print "BFS: ", bfs_path4

    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expected_path5 = ['1', '4', '12', '32']
    brute_path5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    bfs_path5 = directedBFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expected_path5
    print "Brute-force: ", brute_path5
    print "BFS: ", bfs_path5

    # Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expected_path6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brute_path6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
    bfs_path6 = directedBFS(digraph, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expected_path6
    print "Brute-force: ", brute_path6
    print "BFS: ", bfs_path6

    # Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    bfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedBFS(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did BFS search raise an error?", bfsRaisedErr

    # Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    bfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedBFS(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did BFS search raise an error?", bfsRaisedErr