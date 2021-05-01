import sys
from random import randint


def nwd(aa, bb):
    while bb:
        aa, bb = bb, aa % bb
    return aa


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


def solv(x, y):
    nw = nwd(x, y)
    return 1 + solv(x/nw, y/nw) if nw != 1 else 0


mem = {}


def cnt(n):
    on = n
    if n in mem:
        return mem[n]
    cn = 0
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            cn += 1
        k += 1

    mem[on] = cn
    return cn


g = Graph()

INF = float('inf')
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

src = 0
sink = n+1

g.addVertex(src)
g.addVertex(sink)

for i in range(1, n+1):
    g.addVertex(i)
    if i % 2:
        g.addEdge(src, i, cnt(a[i]))
    else:
        g.addEdge(i, sink, cnt(a[i]))


for i in range(m):
    x, y = map(int, input().split())

    g.addEdge(x if x % 2 else y, y if x % 2 else x, solv(x, y))

print(g.maxFlow(src, sink))
