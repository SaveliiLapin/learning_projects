n = float(input())
summa = 1

while n != 1:
    summa += 1 / (n ** 2)
    n -= 1

print(summa)
