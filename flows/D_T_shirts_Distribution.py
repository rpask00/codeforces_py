import sys
from random import randint

class Graph:
    verticies = {}
    nodesCount = 0

    class Vertex:
        def __init__(self, label, endPoint=None):
            self.label = label
            self.edges = []
            self.visitedToken = 0
            self.endPoint = endPoint

    class Edge:
        residual = None

        def __init__(self, from_, to_, isResidual, maxCapacity):
            self.from_ = from_
            self.to_ = to_
            self.isResidual = isResidual
            self.capacity = maxCapacity
            self.flow = 0

        def augment(self, bootleneck):
            self.flow += bootleneck
            self.residual.flow -= bootleneck

        def remainingCapacity(self):
            return self.capacity - self.flow

    def addEdge(self, from_, to_, capacity):
        from_ = self.verticies[from_]
        to_ = self.verticies[to_]
        if from_.endPoint and from_.endPoint != to_:
            from_ = from_.endPoint

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

    def addVertex(self, label, *args):
        self.nodesCount += 1
        if args:
            capacity = args[0]
            key = str(randint(0, sys.maxsize)) + '--' + str(label)
            endPoint = self.Vertex(key)
            self.verticies[key] = endPoint
            self.verticies[label] = self.Vertex(label,  endPoint=endPoint)
            self.addEdge(label, key, capacity)

        else:
            self.verticies[label] = self.Vertex(label)

    def maxFlow(self, f, t):
        f = self.verticies[f]
        t = self.verticies[t]
        visitedToken = 1
        flow = 0

        def dfs(node, bootleneck=sys.maxsize):
            node.visitedToken = visitedToken
            bootleneck_backup = bootleneck

            if node == t:
                return bootleneck

            for edge in node.edges:
                if edge.remainingCapacity() == 0 or edge.to_.visitedToken == visitedToken:
                    continue

                bootleneck = dfs(edge.to_, min(
                    bootleneck, edge.remainingCapacity()))
                if bootleneck:
                    edge.augment(bootleneck)
                    return bootleneck
                else:
                    bootleneck = bootleneck_backup

            return 0

        while True:
            bootleneck = dfs(f)

            if not bootleneck:
                break

            flow += bootleneck
            visitedToken += 1

        return flow

def solve():
    g = Graph()
    sink = 12
    g.addVertex(sink)
    vc = 0
    have = list(map(int, input().split()))

    szs = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    n = int(input())

    supply = []
    wants = [0, 0, 0, 0, 0]
    order = []
    g.addVertex(vc)
    vc += 1

    res = ['' for i in range(n)]

    for i in range(11):
        g.addVertex(vc)
        vc += 1

    for _ in range(n):
        s = input().split(',')
        if len(s) == 1:
            have[szs.index(s[0])] -= 1
            n -= 1
            res[_] = s[0]
            if have[szs.index(s[0])] < 0:
                return print('NO')
        else:
            order.append(szs.index(s[0]))
            wants[szs.index(s[0])] += 1

    for i in range(6):
        g.addEdge(0, i+1, have[i])

    g.addEdge(1, 7, sys.maxsize)

    g.addEdge(2, 7, sys.maxsize)
    g.addEdge(2, 8, sys.maxsize)

    g.addEdge(3, 8, sys.maxsize)
    g.addEdge(3, 9, sys.maxsize)

    g.addEdge(4, 9, sys.maxsize)
    g.addEdge(4, 10, sys.maxsize)

    g.addEdge(5, 10, sys.maxsize)
    g.addEdge(5, 11, sys.maxsize)

    g.addEdge(6, 11, sys.maxsize)

    for i in range(5):
        g.addEdge(7+i, sink, wants[i])


    if g.maxFlow(0, sink) == n:
        print('YES')

        for i in range(1, 7):
            for e in g.verticies[i].edges:
                if not e.isResidual:
                    supply.append(e.flow)

        for i in range(len(res)):
            if not res[i]:
                want = order.pop(0)
                if supply[want*2]:
                    supply[want*2] -= 1
                    res[i] = szs[want]
                else:
                    supply[want*2+1] -= 1
                    res[i] = szs[want+1]

        print('\n'.join(res))
    else:
        print('NO')


solve()
