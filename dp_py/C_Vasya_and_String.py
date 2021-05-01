n, k = map(int, input().split())
mp = input()

c = {'a': 0, 'b': 0}
aa = 0
l = 0

for m in mp:
    c[m] += 1

    if min(c['a'], c['b']) > k:
        c[mp[l]] -= 1
        l += 1
    else:
        aa += 1

print(aa)
