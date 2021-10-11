def xor(xx, yy):
    if xx:
        if yy:
            return 0
        else:
            return 1
    else:
        if yy:
            return 1
        else:
            return 0


x = int(input())
y = int(input())

print(xor(x, y))
