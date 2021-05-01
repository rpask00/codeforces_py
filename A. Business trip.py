import sys

k = int(input())
mths = list(map(int, input().split(' ')))


def solve(c, cnt, index):
    if c <= 0:
        return cnt

    if index > 11:
        return sys.maxsize

    return min(solve(c-mths[index], cnt+1, index+1), solve(c, cnt, index+1))


res = solve(k, 0, 0)
if res == sys.maxsize:
    res = -1
print(res)
