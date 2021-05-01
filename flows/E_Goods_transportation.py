from random import randint

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# n, m = 10000, 100
# b = [randint(1, 100) for _ in range(n)]
# a = [randint(1, 100) for _ in range(n)]

r = 0

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] == 0:
            break

        rm = min([b[j], a[i], m])
        r += rm
        a[i] -= rm
        b[j] -= rm

    
    rm = min(b[i], a[i])
    r += rm
    a[i] -= rm
    b[i] -= rm


\
print(r)
