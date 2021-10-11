def IsPointInArea(x, y):
    inside_circle = (abs(x + 1) ** 2 + abs(y - 1) ** 2) ** 0.5 <= 2
    outside_circle = (abs(x + 1) ** 2 + abs(y - 1) ** 2) ** 0.5 >= 2
    above_plus = y >= 2 * (x + 1)
    below_plus = y <= 2 * (x + 1)
    above_minus = y >= -x
    below_minus = y <= -x
    is_in_above_area = inside_circle and above_plus and above_minus
    is_in_below_area = outside_circle and below_plus and below_minus

    return is_in_above_area or is_in_below_area


xx = float(input())
yy = float(input())

if IsPointInArea(xx, yy):
    print('YES')
else:
    print('NO')
