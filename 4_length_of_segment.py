def distance(x1, y1, x2, y2):
    return (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5


xx1 = float(input())
yy1 = float(input())
xx2 = float(input())
yy2 = float(input())

print(distance(xx1, yy1, xx2, yy2))
