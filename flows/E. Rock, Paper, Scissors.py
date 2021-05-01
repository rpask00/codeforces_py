import sys

class Graph:
    verticies = {}
    nodesCount = 0

    class Vertex:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.visitedToken = 0

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

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

    def addVertex(self, label):
        self.nodesCount += 1
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


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
g = Graph()

for i in range(0, 8):
    g.addVertex(i)

for i in range(3):
    g.addEdge(0, i+1, a[i])

for i in range(3):
    g.addEdge(i+4, 7, b[i])

g.addEdge(1, 4, a[0])
g.addEdge(1, 6, a[0])
g.addEdge(2, 4, a[1])
g.addEdge(2, 5, a[1])
g.addEdge(3, 5, a[2])
g.addEdge(3, 6, a[2])

print(n-g.maxFlow(0, 7), min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0]))
