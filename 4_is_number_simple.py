def IsPrime(n):
    num = 2

    while num <= n ** 0.5:
        if n % num == 0:
            return False
        num += 1

    return True


nn = int(input())

if IsPrime(nn):
    print('YES')
else:
    print('NO')
