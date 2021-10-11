def sum():
    a = int(input())
    if a == 0:
        return a
    else:
        return a + sum()


print(sum())
