
t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    if max(a) <= d:
        print('YES')
    else:
        print('YES' if a[0] + a[1] <= d else 'NO')
        

