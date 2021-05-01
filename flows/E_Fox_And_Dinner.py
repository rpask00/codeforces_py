def main():
    sieve = [False, True] * 10001
    for i in range(3, 140, 2):
        if sieve[i]:
            j, k = i * 2, i * i
            le = (20001 - k) // j + 1
            sieve[k::j] = [False] * le
 
    n = int(input())
    aa = list(map(int, input().split()))
    pp = [-1] * n
 
    def dsu_get(v):
        if dsu[v] != v:
            dsu[v] = dsu_get(dsu[v])
        return dsu[v]
 
    def dfs(v):
        if free[v]:
            free[v], a, pv = False, aa[v], pp[v]
            for i, p in enumerate(pp):
                if sieve[a + aa[i]] and pv != i and (p == -1 or dfs(p)):
                    pp[i] = v
                    return True
        return False
 
    for i in range(n):
        free = [True] * n
        if not dfs(i):
            print('Impossible')
            return
    dsu = list(range(n))
    for i, p in enumerate(pp):
        i, p = dsu_get(i), dsu_get(p)
        dsu[p] = i
 
    print(sum(dsu_get(i) == i for i in range(n)))
    for i in range(n):
        if dsu_get(i) == i:
            row = [sum(dsu_get(j) == i for j in range(n)), i + 1]
            j = pp[i]
            while j != i:
                row.append(j + 1)
                j = pp[j]
            print(*row)
 
 
if __name__ == '__main__':
    main()
 
 