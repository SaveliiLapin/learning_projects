def squares(x):
    if x == 1:
        print(1, end=' ')
        return 1
    else:
        print(int(x ** 0.5), end=' ')
        if x - int(x ** 0.5) ** 2 == 0:
            return 0
        else:
            return squares(x - int(x ** 0.5) ** 2)


n = int(input())
squares(n)
