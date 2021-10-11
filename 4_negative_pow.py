def power(a, n):
    ans = 1

    if n == 0:
        return 1
    elif n > 0:
        while n != 0:
            ans *= a
            n -= 1
    else:
        while n != 0:
            ans *= a
            n += 1
        ans = 1 / ans

    return ans


aa = float(input())
nn = int(input())

print(power(aa, nn))
