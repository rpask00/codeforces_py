
INF = float('inf')
n, m = map(int, input().split())
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
comingOut = [[0 for _ in range(n+1)] for _ in range(n+1)]
edges = []
verticies = set()

def floydWarshall():
    for k in range(n+1):
        for i in range(n+1):
            if i == k:
                continue
            for j in range(n+1):
                if j == k or j == i:
                    continue

                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]


for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))
    verticies.add(a)
    verticies.add(b)
    dp[a][a] = 0
    dp[b][b] = 0
    dp[a][b] = w
    dp[b][a] = w

floydWarshall()

for e in edges:
    a, b, w = e
    for v in verticies:
        if dp[v][a] + w == dp[v][b]:
            comingOut[v][b] += 1

        if dp[v][b] + w == dp[v][a]:
            comingOut[v][a] += 1

ans = []

for source in range(1, n+1):
    for dest in range(source+1, n+1):
        count = 0
        if source in verticies and dest in verticies:
            for mid in verticies:
                if dp[source][mid] + dp[mid][dest] == dp[source][dest]:
                    count += comingOut[source][mid]

        ans.append(str(count))


print(' '.join(ans))
