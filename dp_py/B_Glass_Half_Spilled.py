n = int(input())
Ai = []
Bi = []
B = 0
A = 0


def printres(arr):
    mx = 0
    for a, b in enumerate(arr):
        if b:
            mx = max(mx, min(a, b/2+B/2))

    print(mx, end=' ')


for i in range(n):
    a, b = map(int, input().split())
    b = max(b, 0.00000000000000000000000000001)
    Ai.append(a)
    Bi.append(b)
    A += a
    B += b


l1 = [[0 for i in range(A+1)] for i in range(n+1)]
l2 = [[0 for i in range(A+1)] for i in range(n+1)]


for i in range(1, n+1):
    for j in range(i, n+1):
        l1[j][Ai[i-1]] = max(Bi[i-1], l1[j][Ai[i-1]])

printres(l1[-1])

for k in range(2, n+1):
    for i in range(k, n+1):
        for j in range(A+1):
            if k % 2:
                pk = l1[i-1][j]
                pki = l2[i-1][j-Ai[i-1]]
                l1[i][j] = max(
                    pk, pki + Bi[i-1]) if pki else max(pk, l1[i][j])

            else:
                pk = l2[i-1][j]
                pki = l1[i-1][j-Ai[i-1]]
                l2[i][j] = max(
                    pk, pki + Bi[i-1]) if pki else max(pk, l2[i][j])

    printres(l1[-1] if k % 2 else l2[-1])
