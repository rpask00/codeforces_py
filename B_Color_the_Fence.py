v = int(input())
a = [1000000000000] + list(map(int, input().split()))
d = 0
for i in range(9, 0, -1):
    if a[i] == min(a):
        d = i
        break

l = v // a[d]

rest = v - l* a[d]

essa = []

while rest:
    for i in range(9, d, -1):
        if a[i] -  a[d] <= rest:
            rest -= a[i] -  a[d]
            essa.append(str(i))
            break
    else:
        break

res = ''.join(essa) + ''.join([str(d)]*(l-len(essa)))
print(res if res else -1)
