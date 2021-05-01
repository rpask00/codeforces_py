n, k = 4,2
ans = 1
ct = n
spoils = [0, 1, 1, 2, 9]
 
for i in range(2, k + 1):
    ct = ct*(n - i + 1) // i
    ans += ct*spoils[i]
print(ans)