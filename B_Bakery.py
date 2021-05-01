import heapq
 
n, m, k = map(int, input().split())
# matrix = [[] for _ in range(n)]
# visited = [False for _ in range(n)]
edges = []
for i in range(m):
    u, v, l = map(int, input().split())
    edges.append((l, u, v))
    # matrix[u].append((v, l))
    # matrix[v].append((u, l))
 
storage=[]
if k:
    storage =set( map(int, input().split()))
heapq.heapify(edges)
 
while edges:
    edge = heapq.heappop(edges)
    if edge[2] in storage and edge[1] not in storage:
        print(edge[0])
        break
 
    elif edge[1] in storage and edge[2] not in storage:
        print(edge[0])
        break
 
else:
    print(-1)