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


g = Graph()


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

g.addVertex(0)

for i in range(1, n+1):
    g.addVertex(i)
    g.addVertex(n+i)

g.addVertex(2*n+1)

for i in range(m):
    x, y = map(int, input().split())

    g.addEdge(x, n+y, a[x])
    g.addEdge(y, n+x, a[y])

for i in range(1, n+1):
    g.addEdge(0, i, a[i])
    g.addEdge(n+i, 2*n+1, b[i])

    g.addEdge(i, n+i, a[i])


if g.maxFlow(0, 2*n+1) == sum(a) == sum(b):
    print('YES')
    for i in range(1, n + 1):
        row = [0 for _ in range(n)]
        for e in g.verticies[i].edges:
            if not e.isResidual:
                row[e.to_.label-n-1] = e.flow

        print(' '.join(map(str, row)))
else:
    print('NO')
