n = int(input())
lw = list(map(int, input().split()))
adj = [[] for _ in range(n)]
lcnt = [0 for _ in range(n)]
dp = [[0 for _ in range(n)] for __ in range(n)]
order = [i for i in range(n)]
lcnt[0] = 1

for i in range(n-1):
    dp[i] = 1
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
    lcnt[a] += 1
    lcnt[b] += 1
    
dp[-1][-1] = 1

run = True
while run:
    leafs = [i for i, c in enumerate(lcnt) if c == 1]
    run = True if leafs else False

    while leafs:
        leaf = leafs.pop()
        lcnt[leaf] = 0

        while adj[leaf]:
            nx = adj[leaf].pop()

            if lcnt[nx]:
                lcnt[nx] -= 1
                lw[nx] += lw[leaf]
                dp[nx].add(leaf)
adj.clear()
lcnt.clear()
order.sort(key=lambda i: lw[i])
top = [order.pop()]

while order:
    o = order.pop()
    for t in top:
        if not dp[t].intersection(dp[o]):
            print(lw[o]+lw[t])
            break
    else:
        top.append(o)
        continue

    break

else:
    print('Impossible')
