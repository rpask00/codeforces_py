def tim(x, y, x1, y1):
    return abs(x-x1) + abs(y-y1)


r, n = map(int, input().split(' '))
dp = [0 for _ in range(n)]
celebs = []
for i in range(n):
    celebs.append(list(map(int, input().split())))  # t,x,y

celebs = [celeb for celeb in celebs if tim(
    1, 1, celeb[1], celeb[2]) <= celeb[0]]

for i, celeb in enumerate(celebs):
    t1, x1, y1 = celeb
    prevs = [1]

    for j in range(i-1, -1, -1):
        t2, x2, y2 = celebs[j]
        if tim(x1, y1, x2, y2) > t1 - t2:
            continue

        prevs.append(dp[j]+1)

        if dp[j] == max(dp):
            break

    dp[i] = max(prevs)

print(max(dp))
