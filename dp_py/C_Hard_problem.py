INF = float('inf')
n = int(input())
s = []
sr = []
cost = list(map(int, input().split()))
dp = [[], [], [], []]


for i in range(n):
    c = input()
    s.append(c)
    sr.append(c[::-1])

for i in range(1, n):
    if s[i-1] <= s[i]:
        dp[0].append(0)
    else:
        dp[0].append(INF)

    if s[i-1] <= sr[i]:
        dp[1].append(cost[i])
    else:
        dp[1].append(INF)

    if sr[i-1] <= s[i]:
        dp[2].append(0)
    else:
        dp[2].append(INF)

    if sr[i-1] <= sr[i]:
        dp[3].append(cost[i])
    else:
        dp[3].append(INF)


dp[2][0] += cost[i-1]
dp[3][0] += cost[i-1]

r = 0
nr = 0

for i in range(n-1):
    ss = dp[0][i]
    sr = dp[1][i]
    rs = dp[2][i]
    rr = dp[3][i]

    if min([ss, sr, rs, rr]) == INF:
        print(-1)
        break

    nr, r = min(r + rs, ss + nr), min(sr + nr, rr + r)


else:
    print(min(nr, r))
