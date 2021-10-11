def sum(a, b):
    if b != 0:
        return sum(a + 1, b - 1)
    return a


aa = int(input())
bb = int(input())

print(sum(aa, bb))
