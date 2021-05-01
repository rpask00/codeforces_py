from math import *

for i in range(int(input())):
    a, b = map(int, input().split())
    x = 0
    if b == 1:
        x += 1

    n = x + floor(log(a, b+x)) + 1

    while True:
        x += 1
        d = floor(log(a, b+x))+1

        if x + d > n:
            break

        n = x + d

    print(n)
