def fast_pow(aa, nn):
    if nn == 0:
        return 1
    elif nn % 2 == 0:
        return fast_pow(aa ** 2, nn // 2)
    elif nn != 1:
        return aa * fast_pow(aa, nn - 1)
    else:
        return aa


a = float(input())
n = int(input())

print(fast_pow(a, n))
