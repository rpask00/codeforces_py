n = int(input())
a = input()
b = input()
d = [0 for i in range(n)]

i = 0
for s in a:
    if s != b[i]:
        d[i] = 1
    i += 1


i = 0
res = 0

while(i+1 < n):
    if d[i] and d[i+1]:
        if a[i] != a[i+1]:
            res += 1
            d[i] = 0
            d[i+1] = 0
            i += 2
        else:
            i += 1
    else:
        i += 1

print(res + sum(d))
