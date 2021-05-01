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
            # print(bootleneck)
            if not bootleneck:
                break

            flow += bootleneck
            visitedToken += 1

        return flow


g = Graph()


from collections import deque
class Dinic():
    def __init__(self, listEdge, s, t):
        self.s = s
        self.t = t
        self.graph = {}
        self.maxCap = 1000000
        # dict các node lân cận

        # e[0]: from,  e[1]: to,  e[2]: dung luong
        for e in listEdge:

            if e[0] not in self.graph:
                self.graph[e[0]] = []

            if e[1] not in self.graph:
                self.graph[e[1]] = []
                # to     #cap   #reveser edge
            self.graph[e[0]].append([e[1], e[2],  len(self.graph[e[1]])])
            self.graph[e[1]].append([e[0],    0,  len(self.graph[e[0]])-1])

        self.N = len(self.graph.keys())

    def bfs(self):
        self.dist = {}
        self.dist[self.s] = 0
        self.curIter = {node: [] for node in self.graph}

        Q = deque([self.s])

        while(len(Q) > 0):
            cur = Q.popleft()

            for index, e in enumerate(self.graph[cur]):
                # Chỉ add vào các node kế tiếp nếu dung lượng cạnh > 0 và chưa được visit trước đấy
                if e[1] > 0 and e[0] not in self.dist:
                    self.dist[e[0]] = self.dist[cur] + 1
                    # add vào danh sách node kế tiếp của node hiện tại
                    self.curIter[cur].append(index)
                    Q.append(e[0])

    def findPath(self, cur, f):
        if cur == self.t:
            return f

        while len(self.curIter[cur]) > 0:
            indexEdge = self.curIter[cur][-1]
            nextNode = self.graph[cur][indexEdge][0]
            remainCap = self.graph[cur][indexEdge][1]
            indexPreEdge = self.graph[cur][indexEdge][2]

            if remainCap > 0 and self.dist[nextNode] > self.dist[cur]:
                #self.next[cur] = indexEdge
                flow = self.findPath(nextNode,  min(f, remainCap))

                if flow > 0:
                    self.path.append(cur)
                    self.graph[cur][indexEdge][1] -= flow
                    self.graph[nextNode][indexPreEdge][1] += flow
                    # if cur == self.s:
                    #    print(self.path, flow)
                    return flow
                # else:
                    # self.path.pop()
            self.curIter[cur].pop()

        return 0

    def maxFlow(self):
        maxflow = 0
        flow = []

        while(True):
            self.bfs()

            if self.t not in self.dist:
                break

            while(True):
                self.path = []
                f = self.findPath(self.s, self.maxCap)
                #print('iter', self.curIter)
                if f == 0:
                    break

                flow.append(f)
                maxflow += f

        return maxflow

    # Tìm tập node thuộc S và T
    # sau khi đã tìm được max flow
    def residualBfs(self):
        Q = deque([self.s])
        side = {self.s: 's'}

        while(len(Q) > 0):
            cur = Q.popleft()

            for index, e in enumerate(self.graph[cur]):
                if e[1] > 0 and e[0] not in side:
                    Q.append(e[0])
                    side[e[0]] = 's'

        S = []
        T = []
        for x in self.graph:
            if x in side:
                S.append(x)
            else:
                T.append(x)
        return set(S), set(T)
