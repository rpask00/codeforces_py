class Graph:
    class Edge:
        def __init__(self, from_, to_):
            self.from_ = from_
            self.to_ = to_

    class Node:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.visited = False

        def visit(self):
            self.visited = True

    edges = []
    verticies = {}

    def addNode(self, label):
        self.verticies[label] = self.Node(label)

    def addEdge(self, from_, to_):
        if from_ not in self.verticies:
            self.addNode(from_)

        if to_ not in self.verticies:
            self.addNode(to_)

        self.verticies[from_].edges.append(
            self.Edge(self.verticies[from_], self.verticies[to_]))
