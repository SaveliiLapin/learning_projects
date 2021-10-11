def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


xx = float(input())
yy = float(input())

if IsPointInSquare(xx, yy):
    print('YES')
else:
    print('NO')
