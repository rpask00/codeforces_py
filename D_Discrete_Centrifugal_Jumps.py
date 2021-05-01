def empty(l):
    return len(l) == 0


# n = int(input())
# h = list(map(int, input().split(" ")))

# inc, dec = [0], [0]


# dp = [0]*n
# for i in range(1, n):
#     dp[i] = dp[i-1] + 1
#     while not empty(inc) and h[i] >= h[inc[-1]]:
#         x = h[inc.pop()]
#         if h[i] > x and not empty(inc):
#             dp[i] = min(dp[i], dp[inc[-1]] + 1)

#     while not empty(dec) and h[i] <= h[dec[-1]]:
#         x = h[dec.pop()]
#         if h[i] < x and not empty(dec):
#             dp[i] = min(dp[i], dp[dec[-1]] + 1)

#     inc.append(i)
#     dec.append(i)

# print(dp[-1])

n = int(input())
h = list(map(int, input().split(" ")))

inc, dec = [0], [0]
dp = [0]*n
for i in range(1,n):
    dp[i] = dp[i-1]+1
    while not empty(inc) and h[i] >= h[inc[-1]]:
        x = h[inc.pop()]
        if h[i] > x and not empty(inc):
            dp[i] = min(dp[i], dp[inc[-1]]+1)

    while not empty(dec) and h[i] <= h[dec[-1]]:
        x = h[dec.pop()]
        if h[i] < x and not empty(dec):
            dp[i] = min(dp[i], dp[dec[-1]] + 1)

    inc.append(i)
    dec.append(i)

print(dp[-1])
