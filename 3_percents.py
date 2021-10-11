p = int(input())
x = int(input())
y = int(input())

rubles = int((x * 100 + y) * (1 + p / 100) / 100)
kopeiks = int(((x * 100 + y) * (1 + p / 100) + 10 ** -6) % 100)

print(rubles, kopeiks)
