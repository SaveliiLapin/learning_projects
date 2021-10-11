def ReduceFraction(n, m):
    if n % m == 0:
        return nn // m, mm // m
    else:
        return ReduceFraction(m, n % m)


nn = int(input())
mm = int(input())

print(*ReduceFraction(nn, mm))
