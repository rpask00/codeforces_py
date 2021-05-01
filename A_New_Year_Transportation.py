n, t = map(int, input().split())
a = map(int, input().split())

visited = [False for _ in range(n)]
matrix = [[] for _ in range(n)]

for i, aa in enumerate(a):
    matrix[i].append(i+aa)


visited[0] = True
que = [0]

while que:
    node = que.pop(0)

    if node == t-1:
        print('YES')
        break

    for nxt in matrix[node]:
        if not visited[nxt]:
            visited[nxt] = True
            que.append(nxt)
else:
    print('NO')
