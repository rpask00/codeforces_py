for i in range(int(input())):
    res = 0
    n = int(input())

    while(n):
        if(n < 2050):
            print(-1)
            break

        s = str(n)
        zr = max(len(s) - 4, 0)
        x = int("2050" + '0'*zr)
        if(x > n):
            zr -= 1
            if(zr < 0):
                print(-1)
                break
            x = int("2050" + '0'*zr)
            
        d = n//x
        n -= x*d

        res += d
    else:
        print(res)
