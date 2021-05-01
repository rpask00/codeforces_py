
import sys
INF = float('inf')
q = int(input())


for _ in range(q):
    n = int(input())
    t = list(sorted(map(int, input().split())))
    # dp = [[INF for ___ in range(2 * n+1)] for __ in range(n)]

    # dp[0][1] = t[0] - 1

    # for j in range(2, n+1):
    #     dp[0][j] = min(abs(t[0] - j), dp[0][j-1])

    # for i in range(1, n):
    #     for j in range(i+1, n+1):
    #         dp[i][j] = min(abs(t[i] - j) + dp[i-1][j-1], dp[i][j-1])

    # print(min(dp[n-1]))

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

    g = Graph()
    g.addVertex(0)
    g.addVertex(3*n+1)

    for i in range(1, 3*n+1):
        g.addVertex(i)

    for i in range(1, n+1):
        g.addEdge(0,i,1)

    for i in range(n+1, 3*n+1):
        g.addEdge(i,3*n+1,1)


    for i in range(1, n):
        for j in range(n+1, 3*n+1):
            g.addEdge(i, j, abs(t[i-1]-j))

    def maxFlow(f, t):
        f = g.verticies[f]
        t = g.verticies[t]
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

    print(maxFlow(0, 3*n+1))
