def dis(xx1, yy1, xx2, yy2):
    return (abs(xx2 - xx1) ** 2 + abs(yy2 - yy1) ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

per = dis(x1, y1, x2, y2) + dis(x1, y1, x3, y3) + dis(x2, y2, x3, y3)
print('{:.6f}'.format(per))
