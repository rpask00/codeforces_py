n = int(input())
d = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp1[0] = 0 if d[0] & 1 else 1
dp2[0] = 0 if d[0] & 2 else 1


for i in range(1, n):
    if d[i] == 3:
        dp1[i], dp2[i] = dp2[i-1], dp1[i-1]
    elif d[i] == 2:
        dp1[i], dp2[i] = min(dp1[i-1], dp2[i-1])+1, dp1[i-1]
    elif d[i] == 1:
        dp1[i],  dp2[i] = dp2[i-1], min(dp1[i-1], dp2[i-1])+1
    elif d[i] == 0:
        dp2[i] = dp1[i] = min(dp1[i-1], dp2[i-1])+1

print(min(dp2[n-1], dp1[n-1]))
