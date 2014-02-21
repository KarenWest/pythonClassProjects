# 6.00 Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#


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


class SmartNode(Node):

    def __hash__(self):
        return int(self.name)


class Edge(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return '%s->%s' % (str(self.src), str(self.dest))


class WeightedEdge(Edge):

    def __init__(self, src, dest, total_distance, distance_outdoors):
        super(WeightedEdge, self).__init__(src, dest)
        self.total_distance = total_distance
        self.distance_outdoors = distance_outdoors


class Path(object):

    def __init__(self, nodes_visited, total_distance, distance_outdoors):
        self._nodes_visited = list(nodes_visited)
        self.total_distance = total_distance
        self.distance_outdoors = distance_outdoors

    def is_node_visited(self, node):
        return node in self._nodes_visited

    def is_end_reached(self, end):
        return self._nodes_visited[-1].getName() == end

    def get_node_list(self):
        return [str(node) for node in self._nodes_visited]

    def get_current_position(self):
        return self._nodes_visited[-1]

    def add_edge(self, edge):
        self.total_distance += edge.total_distance
        self.distance_outdoors += edge.distance_outdoors
        self._nodes_visited.append(edge.getDestination())

    def clone(self):
        return Path(self._nodes_visited,
                    self.total_distance,
                    self.distance_outdoors)

    def __str__(self):
        return ' => '.join(str(node) for node in self._nodes_visited)


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
            for d in self.edges[str(k)]:
                res = '%s%s->%s\n' % (res, str(k), str(d))
        return res[:-1]


class SmartDigraph(Digraph):

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(edge)
