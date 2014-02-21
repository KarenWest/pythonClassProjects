from util import *

def DFS(graph, start, end, mazeWidth, mazeHeight, wallCoordList, path = Stack(), shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    wallNodeList = []
    for x in range(mazeWidth):
        for y in range(mazeHeight):
            for wall in wallCoordList: #wall = (x,y) tuple where wall located
                    if wall == (x,y):
                        nodeNum = (x * mazeWidth) + y
                        wallNodeList.append(Node(nodeNum))
#(x * mazeWidth) + y = nodeNum in graph 
#Note: Stack.pop() = list.pop(obj=list[-1]) --takes last element from list                   
#list.append(x)--Add an item to the end of the list; equivalent to 
# a[len(a):] = [x].
#list1+list2. This gives a new list that is the concatenation of list1 
#and list2.
#self.list.append(item) = Stack.pop()
    path.push(start) #push node onto stack (append to list)
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        #avoid cycles & avoid walls -- can't go through them in path
        if (node not in path) and (node not in wallNodeList):
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path)
                if newPath != None:
                    shortest = newPath
    return shortest



def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath(sp)
