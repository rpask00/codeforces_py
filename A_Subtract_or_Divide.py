import math

n = int(input())

for i in range(n):
    d, k = map(int, input().split())
    x = math.floor(d*math.sqrt(2) / (2*k))
    if ((x+1)*k)**2 + ((x)*k)**2 > d**2:
        print('Utkarsh')
    else:
        print('Ashish')
