def solve(n, s):
    if n == 0:
        return s

    if n < 3:
        return False

    s[0] += 1
    three = solve(n-3, s)
    if three:
        return three
    s[0] -= 1
    s[1] += 1
    five = solve(n-5, s)
    if five:
        return five
    s[1] -= 1
    s[2] += 1
    seven = solve(n-7, s)
    if seven:
        return seven
    s[2] -= 1


for t in range(int(input())):
    res = []

    n = int(input())

    res = solve(n, [0, 0, 0])
    if res:
        print(' '.join(map(str, res)))
    else:
        print(-1)


