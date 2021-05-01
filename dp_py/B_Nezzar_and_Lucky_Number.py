
for i in range(int(input())):
    n, d = map(int, input().split())
    lista = list(map(int, input().split()))

    for l in lista:
        c = l // d
        r = l % d

        if (str(d) in str(l)):
            print("YES")
        else:
            if c >= 10:
                print("YES")
            else:
                while(c):
                    if (r % 10 == d):
                        print('YES')
                        break
                    else:
                        c -= 1
                        r += d
                else:
                    print('NO')
