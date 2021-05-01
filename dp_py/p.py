t = int(input())
c = 1
s = int(input())
for _ in range(t-1):
    n = int(input())
    s += n

    k = 1
    for i in range(1, n):
        k = k*(s-i)//i
    c = (c*k) % (10**9+7)
print(c)
