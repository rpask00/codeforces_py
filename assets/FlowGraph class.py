import heapq
import sys
INF = float('inf')


class FlowGraph:
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



fg = FlowGraph()
