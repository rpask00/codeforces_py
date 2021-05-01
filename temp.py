M = {}


def cal(footmen, horses, footcnt, horsecnt):
    if min(footmen, horses, footcnt, horsecnt) < 0:
        return 0
    if footmen == 0 and horses == 0:
        return 1
    v = (footmen, horses, footcnt, horsecnt)
    if not v in M:
        M[v] = (cal(footmen-1, horses, footcnt-1, y) + cal(footmen, horses-1, x, horsecnt-1)) % 10**8
    return M[v]


n, m, x, y = map(int, input().split())
print(cal(n, m, x, y))
