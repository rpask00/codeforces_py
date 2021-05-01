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


n, M = map(int, input().split())
weigts = set()
edges = []

for i in range(M):
    a, b, d = map(int, input().split())
    weigts.add(d)
    edges.append((a, n + b, d))

weigts = list(weigts)
weigts.sort()
edges =sorted(edges,key=lambda x: x[2])
pipes = []
src = 0
sink = 2*n+1

for i in range(1, n+1):
    pipes.append((src, i, 1))


for i in range(n+1, sink):
    pipes.append((i, sink, 1))


l = 0
mid = 0
r = 10**9
f = 0

while l <= r:
    mtr = []
    mid = (l+r)//2
    for e in edges:
        if e[2] >= mid:
            break

        mtr.append(e)

    g = Dinic(mtr + pipes, src, sink)

    if g.maxFlow() == n:
        f = -1
        # if r == mid:
        #     break
        r = mid+1
    else:
        # if l == mid:
        #     break
        l = mid-1

print(-1 if mid+f == len(weigts) else weigts[mid+f])



