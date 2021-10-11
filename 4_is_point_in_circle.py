def IsPointInCircle(x, y, xc, yc, r):
    return (abs(x - xc) ** 2 + abs(y - yc) ** 2) ** 0.5 <= r


xx = float(input())
yy = float(input())
xcc = float(input())
ycc = float(input())
rr = float(input())

if IsPointInCircle(xx, yy, xcc, ycc, rr):
    print('YES')
else:
    print('NO')
