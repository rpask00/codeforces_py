n = int(input())
a = list(map(int, input().split()))

p = [0]*(n+2)
m = [0]*(n+2)


for i in range(n):
    p[a[i]] = i


for i in range(n, 0, -1):
    j = p[i] % i

    while j < n and m[i] == 0:
        m[i] = i < a[j] and m[a[j]] == 0
        j += i


for i in range(n):
    print('BA'[m[a[i]]], end='')
