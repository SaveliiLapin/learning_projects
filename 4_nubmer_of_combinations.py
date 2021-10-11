def C(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif n == k:
        return 1
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


nn = int(input())
kk = int(input())

print(C(nn, kk))
