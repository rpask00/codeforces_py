import heapq
import sys
INF = float('inf')


class Graph:
    nodes = {}
    nodesCount = 0

    class Node:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.visited = False
            self.level = 0
            self.deadEnd = False

        def markAsNotVisited(self):
            self.visited = False

        def visit(self):
            self.visited = True

    class Edge:
        residual = None

        def __init__(self, from_, to_, isResidual, maxCapacity):
            self.from_ = from_
            self.to_ = to_
            self.isResidual = isResidual
            self.capacity = maxCapacity
            self.flow = 0

        def augment(self, flow):
            self.flow += flow
            self.residual.flow -= flow

        def remainingCapacity(self):
            return self.capacity - self.flow

    def __init__(self, matrix=None):
        if matrix:
            for a, row in enumerate(matrix):
                for b, cap in enumerate(row):
                    if not cap:
                        continue

                    self.addEdge(a, b, cap)

    def addEdge(self, from_, to_, capacity):
        from_ = self.nodes[from_]
        to_ = self.nodes[to_]

        if from_ not in self.nodes:
            self.addNode(from_)

        if to_ not in self.nodes:
            self.addNode(to_)

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

    def addNode(self, label):
        self.nodesCount += 1
        self.nodes[label] = self.Node(label)

    def getNode(self, label):
        return self.nodes[label] if label in self.nodes else None

    def unvisitNodes(self):
        for ver in self.nodes:
            self.getNode(ver).markAsNotVisited()

    def resetLevels(self):
        for ver in self.nodes:
            self.getNode(ver).level = 0
            self.getNode(ver).deadEnd = False


class GraphManager:
    def __init__(self, graph):
        self.graph = graph

    def DinicMaxFlow(self, source, sink):
        source = self.graph.getNode(source)
        sink = self.graph.getNode(sink)
        flow = 0

        def bfs(node):
            bfs_que = [node]
            reached_sink = False
            while bfs_que:
                node = bfs_que.pop(0)
                if node == sink:
                    reached_sink = True

                for edge in node.edges:
                    if not edge.remainingCapacity() or edge.to_.visited:
                        continue

                    edge.to_.visited = True
                    edge.to_.level = node.level + 1
                    bfs_que.append(edge.to_)

            self.graph.unvisitNodes()
            return reached_sink

        def dfs(node, bootleneck=INF, level=0):
            bootleneck_backup = bootleneck
            node.visited = True

            if node == sink:
                return bootleneck

            heap = []

            for i, edge in enumerate(node.edges):
                if not edge.remainingCapacity():
                    continue

                if edge.to_.visited:
                    continue

                if edge.to_.level <= level and edge.to_ != sink:
                    continue

                if edge.to_.deadEnd:
                    continue

                heapq.heappush(heap, (-edge.remainingCapacity(), i, edge))

            while heap:
                maxCapacity, i, edge = heapq.heappop(heap)
                maxCapacity *= -1

                bootleneck = dfs(edge.to_, min(
                    bootleneck, maxCapacity), edge.to_.level)

                if bootleneck:
                    edge.augment(bootleneck)
                    return bootleneck
                else:
                    bootleneck = bootleneck_backup

            node.deadEnd = True
            return 0

        while bfs(source):
            while True:
                bootleneck = dfs(source)

                if not bootleneck:
                    break

                flow += bootleneck
                self.graph.unvisitNodes()

            self.graph.resetLevels()

        return flow


g = Graph()

g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)
g.addNode(5)
g.addNode(6)
g.addNode(7)
g.addNode(8)
g.addNode(9)
g.addNode(10)


g.addEdge(0, 1, 5)
g.addEdge(0, 2, 10)
g.addEdge(0, 3, 15)
g.addEdge(1, 4, 10)
g.addEdge(2, 1, 15)
g.addEdge(2, 5, 20)
g.addEdge(3, 6, 25)
g.addEdge(4, 5, 25)
g.addEdge(4, 7, 10)
g.addEdge(5, 8, 30)
g.addEdge(5, 3, 5)
g.addEdge(6, 8, 20)
g.addEdge(6, 9, 10)
g.addEdge(7, 10, 5)
g.addEdge(8, 10, 15)
g.addEdge(8, 9, 15)
g.addEdge(9, 10, 10)

gm = GraphManager(g)

print(gm.DinicMaxFlow(0, 10))
