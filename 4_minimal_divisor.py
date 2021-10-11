def MinDivisor(n):
    num = 2

    while num <= n ** 0.5:
        if n % num == 0:
            return num
        num += 1

    return n


nn = int(input())

print(MinDivisor(nn))
