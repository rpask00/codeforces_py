
for i in range(int(input())):
    n = int(input())
    d = [0 for i in range(n+1)]
    res = 0
    lista = list(map(int, input().split()))

    for l in lista:
        d[l] += 1

    print(max(d))
