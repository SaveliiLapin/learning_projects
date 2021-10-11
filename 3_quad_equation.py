a = float(input())
b = float(input())
c = float(input())

b *= -1
d = b ** 2 - 4 * a * c

if d == 0:
    print(b / (2 * a))
elif d > 0:
    if (b - d ** 0.5) / (2 * a) < (b + d ** 0.5) / (2 * a):
        print((b - d ** 0.5) / (2 * a), (b + d ** 0.5) / (2 * a))
    else:
        print((b + d ** 0.5) / (2 * a), (b - d ** 0.5) / (2 * a))
