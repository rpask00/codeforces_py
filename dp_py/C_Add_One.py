from sys import stdin, stdout

dp = [0] * 200005

for i in range(0, 9):
    dp[i] = 2

dp[9] = 3

for i in range(10, 200005):
    dp[i] = (dp[i-10] + dp[i-9]) % 1000000007

ans = ''

for i in range(int(input())):
    n, m = stdin.readline().split()
    m = int(m)
    res = 0
    for s in n:
        s = int(s)
        ind = m - (10-s)
        if ind < 0:
            res += 1
            continue

        res = (res + dp[ind]) % 1000000007

    stdout.write(str(res) + "\n")
