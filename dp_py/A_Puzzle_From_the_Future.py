import sys
INF = float('inf')


for i in range(int(input())):
    n = int(input())
    b = input()
    b = [int(x) for x in b]

    d = []
    a = [1]

    d.append(2 if b[0] else 1)

    for i in range(1, n):
        if b[i] + 1 == d[-1]:
            a.append(0)
            d.append(b[i] + a[i])
        else:
            a.append(1)
            d.append(b[i] + a[i])

    print(''.join(map(str, a)))
