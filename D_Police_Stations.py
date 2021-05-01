def key(a, b): return '-'.join(map(str, sorted([a, b])))


n, k, d = map(int, input().split())
ppp = set(map(int, input().split()))
adj = [set() for _ in range(n+1)]
roads = {}

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)
    roads[key(a, b)] = i+1

vis = [0 for _ in range(n+1)]
trm = set()


for p in ppp:
    stack = [(p, 0)]
    vis[p] = 1
    while stack:
        node, lv = stack.pop()

        for nx in adj[node]:
            if nx in ppp or vis[nx] or lv > d:
                trm.add(roads[key(node, nx)])
                continue

            vis[nx] = 1
            adj[nx].discard(node)
            stack.append((nx, lv+1))

print(len(trm))
print(' '.join(map(str, trm)))
