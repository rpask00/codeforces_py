def solve():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())

    dp = []
    for i in range(n):
        dp.append([])
        for j in range(m):
            dp[i].append(dp[i][j - 1] + a[i][j] == '*' if j else a[i][j] == '*')

    answer = 0
    for y in range(n):
        for x in range(m):
            if a[y][x] == '.':
                continue

            for h in range(min(n - y, m - x, x + 1)):
                if dp[y + h][x + h] - (0 if x - h  < 1 else dp[y + h][x - h - 1]) != h * 2 + 1:
                    break

                answer += 1

    print(answer)


tests = int(input())

while (tests > 0):
    solve()
    tests = tests - 1
