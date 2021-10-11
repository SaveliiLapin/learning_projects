import math


def reversal():
    a = int(input())
    b = False

    if a != 0:
        reversal()

        if int(math.sqrt(a)) ** 2 == a or a == 1:
            print(a, end=' ')
            b = True
    return b


if not reversal():
    print(0)
