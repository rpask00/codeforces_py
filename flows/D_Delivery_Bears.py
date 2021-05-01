import sys
from random import randint
from math import ceil


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
        # if from_.endPoint and from_.endPoint != to_:
        #     from_ = from_.endPoint

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

    def maxflowPath(self, f, t):
        vis = [0 for _ in range(len(self.verticies)+1)]
        flows = [0 for _ in range(len(self.verticies)+1)]
        flows[f] = sys.maxsize
        que = [f]
        vis[f] = 1

        while que:
            node = que.pop(0)
            for e in self.verticies[node].edges:
                flows[e.to_.label] = max(
                    min(e.capacity, flows[node]), flows[e.to_.label])

                if not vis[e.to_.label]:
                    que.append(e.to_.label)

                vis[e.to_.label] = 1

        return flows[t]

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


n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
l, r = 0, 1000000

while r-l > 1e-9:
    md = (l+r)/2

    g = Graph()

    for i in range(n):
        g.addVertex(i+1)

    for i in range(m):
        a, b, c = edges[i]
        g.addEdge(a, b, c // md)

    flow = g.maxFlow(1, n)

    if flow >= x:
        l = md
    else:
        r = md


print(x*r)
