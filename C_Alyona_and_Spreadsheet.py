m, n = map(int, input().split())
a = []
g = []

lg = [0] * m

for i in range(m):
    a += [list(map(int, input().split()))]
    g += [[1]*n]

for x in range(n):
    for y in range(1, m):
        if a[y][x] >= a[y-1][x]:
            g[y][x] = g[y-1][x]+1

for y in range(m):
    for x in range(n):
        lg[y] = max(lg[y], g[y][x])

for i in range(int(input())):
    l, r = map(int, input().split())
    print("Yes" if(lg[r-1] >= r-l+1) else "No")
