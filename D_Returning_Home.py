from heapq import *
INF = float('inf')

def dit(xx, yy, x, y): return abs(xx-x) + abs(yy-y)

n, m = map(int, input().split())
xi, yi, xt, yt = map(int, input().split())
s = [xi, yi]
f = [xt, yt]
grapx = [(xi, 0)]
grapy = [(yi, 0)]
adj = [[] for _ in range(m+1)]
adj[0].append((dit(xi, yi, xt, yt), m+1))

for i in range(1, m+1):
    x, y = map(int, input().split())
    heappush(grapx, (x, i))
    heappush(grapy, (y, i))
    adj[i].append((dit(xt, yt, x, y), m+1))


for i in range(2):
    graph = grapy if i else grapx
    prev = heappop(graph)
    while graph:
        curr = heappop(graph)
        d = abs(curr[0] - prev[0])
        adj[prev[1]].append((d, curr[1]))
        adj[curr[1]].append((d, prev[1]))
        prev = curr

D = [INF for _ in range(m+2)]
D[0] = 0
hq = [(0, 0)]

while hq:
    dcur, nd = heappop(hq)

    if nd == m+1:
        continue

    if D[nd] < dcur:
        continue

    for dnx, nx in adj[nd]:
        if D[nx] > dcur + dnx:
            D[nx] = dcur + dnx
            heappush(hq, (D[nx], nx))

print(D[m+1])
