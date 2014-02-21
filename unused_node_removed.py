# 6.00 Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '%s->%s' % (self.src, self.dest)

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
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '%s%s->%s\n' % (res, k, d)
        return res[:-1]

class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
        self.weights = {}
    def addWeights(self, start, end, weights):
        self.weights.setdefault((start,end), []).append(weights)
    def __str__(self):
        return '\n'.join('\n'.join('%s-%s->%s' % (k, p, d) for p in self.weights.get((k,d), ['']))
                         for k in sorted(self.edges)
                         for d in self.edges[k]
                        )