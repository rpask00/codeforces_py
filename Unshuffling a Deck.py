

n = int(input())
c = [int(x) for x in input().split()]
solved = c.copy()
solved.sort()


ans = []

for i in range(1, n):
    for j in range(1, n):
        a = c.index(j)
        b = c.index(j+1)
        z = b+1

        if b > a:
            if a+1 == b and a == solved:
                break

            continue

        z = b+1

        s1 = c[:b]

        while z < a and c[z] == c[z-1]+1:
            z += 1

        s2 = c[b:z]
        s3 = c[z:a+1]
        s4 = c[a+1:]

        c = s4 + s3 + s2 + s1
        ans.append([str(len(x)) for x in [s1, s2, s3, s4] if x])

print(len(ans))
for an in ans:
    print(len(an), ' '.join(an))

