from collections import deque
INF = float('inf')

n, m = map(int, input().split())
d = list(sorted([-INF] + list(map(int, input().split()))))
dsts = [d[i+1] - d[i] for i in range(m)]
g, r = map(int, input().split())
dp = [[0 for __ in range(g)] for i in range(m)]

que = deque([(0, g, 1)])
ans = INF
# ans = INF
while que:
    cy, tl, node = deque.popleft(que)

    if node == m:
        ans = min(ans, cy*(g+r) + (-r if tl == g else g - tl))
        continue

    if dp[node][tl-1]:
        continue

    dp[node][tl-1] = 1
    dl, dr = dsts[node - 1], dsts[node]

    if dl < tl:
        deque.appendleft(que, (cy, tl-dl, node-1))
    elif dl == tl:
        deque.append(que, (cy+1, g, node-1))

    if dr < tl:
        deque.appendleft(que, (cy, tl-dr, node+1))
    elif dr == tl:
        deque.append(que, (cy + 1, g, node+1))


print(ans if ans < INF else -1)
