for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x = abs(x2-x1)
    y = abs(y2-y1)
    bonus = 2 if x and y else 0 
    print(x +  y + bonus)