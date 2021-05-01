
for i in range(int(input())):

    n = int(input())
    lista = list(map(int, input().split()))
    lista.sort()

    for i in range(0, n, 2):
        if lista[i] != lista[i+1]:
            print('NO')
            break
    else:
        print('YES')
