# 6.00 Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#
# Modified by Jimmy Bangun

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)

class Edge(object):
    def __init__(self, src, dest, dist, outd):
        self.src = src
        self.dest = dest
        self.dist = dist
        self.outd = outd
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getDistance(self):
        return self.dist
    def getOutdoor(self):
        return self.outd
    def __str__(self):
        return '%s->%s %s m, with %s m outdoors' % (str(self.src), str(self.dest), str(self.dist), str(self.outd))
        # This has not been tested for correctness

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        dist = edge.getDistance()
        outd = edge.getOutdoor()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        properties = [dest, dist, outd]
        self.edges[src].append(properties)
    def childrenOf(self, node):
        result = []
        for item in self.edges[node]:
            result.append(item[0])
        return result
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '%s%s->%s %s,%s' % (res, str(k), str(d[0]), str(d[1]), str(d[2]))
                # This has not been tested for correctness
        return res[:-1]