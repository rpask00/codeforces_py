
n, h = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n, 0, -1):
    part = list(sorted(a[0:i]))
    if (len(part) % 2) == 0:
        part.insert(0, 0)
    v = sum(part[::2])
    if v <= h:
        print(i)
        break
