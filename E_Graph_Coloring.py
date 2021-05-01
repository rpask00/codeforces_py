n, m = map(int, input().split())
n1, n2, n3 = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):

    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

color = [0]*n

def bfs(v, c):
    color[v] = c
    h = w = 0
    if c == 1:
        h = 1
    else:
        w = 1

    for nxt in adj[v]:
        if color[nxt] == c:
            return [False, h, w ]
        elif color[nxt] == 0:
            f, hh, ww = bfs(nxt, -c)
            h += hh
            w += ww
            if not f:
                return [False, h, w]
    return [True, h, w]


qqq = []
for i in range(n):
    if color[i] == 0:
        f, h, w = bfs(i, 1)
        if not f:
            exit(print("NO"))

        qqq.append([i, min(h, w), abs(h-w), -1 if (h < w) else 1])
remaining2 = n2
for _, i, __, ___ in qqq:
    remaining2 -= i

if remaining2 < 0:
    exit(print("NO"))

dp = [(remaining2+1)*[0]for _ in range(len(qqq)+1)]
dp[0][0] = 1

for q in range(len(qqq)):
    _, __, overflow, ___ = qqq[q]
    for twos in range(remaining2+1):
        dp[q+1][twos] = dp[q][twos]

    for twos in range(remaining2+1):
        if overflow+twos > remaining2:
            break
        dp[q+1][overflow+twos] |= dp[q][twos]

if dp[-1][-1] == 0:
    exit(print("NO"))

k = remaining2
qq = []
for i in range(len(qqq), 0, -1):
    if dp[i][k] == dp[i-1][k]:
        qq.append((qqq[i-1][0], -qqq[i-1][3]))
    else:
        qq.append((qqq[i-1][0], qqq[i-1][3]))
        k -= qqq[i-1][2]

color = [0]*n
visited = set()
for i, c in qq:
    stack = [i]
    visited.add(i)
    color[i] = c
    for j in stack:
        for k in adj[j]:
            if k in visited:
                continue
            visited.add(k)
            color[k] = -color[j]
            stack.append(k)
            
for i in range(n):
    if color[i] == 1:
        color[i] = "2"
    elif n1:
        color[i] = "1"
        n1 -= 1
    else:
        color[i] = "3"
print("YES")
print("".join(color))
