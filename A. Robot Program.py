import math

for ti in range(int(input())):
    sss = input()
    n=  len(sss)-1
    lp = [0 for _ in range(n + 1)]
    rp = [0 for _ in range(n + 1)]
    lo = [0 for _ in range(n + 1)]
    ro = [0 for _ in range(n + 1)]

    for i in range(n+1):
        sl = sss[i]
        sr = sss[n-i]

        if sl == '(':
            lo[i] += lo[i-1] + 1 if i else 1

        elif sl == '[':
            lp[i] += lp[i-1] + 1 if i else 1
    
        lo[i] = max(lo[i], lo[i-1]) if i else  1
        lp[i] = max(lp[i], lp[i-1]) if i else 1

        if sr == ')':
            ro[i] += ro[i-1] + 1 if i else 1


        elif sr == ']':
            rp[i] += rp[i-1] + 1 if i else 1

        ro[i] = max(ro[i], ro[i-1]) if i else  1
        rp[i] = max(rp[i], rp[i-1]) if i else 1


    for i in range(n):

        lo[i] = lo[i] - ro[n-i]
        lp[i] = lp[i] - rp[i+1]

    

    print(max(max(ro), max(lo)) + max(max(rp), max(lp)))
