p = int(input())
x = int(input())
y = int(input())
k = int(input())

while k != 0:
    rubles = int((x * 100 + y) * (1 + p / 100) / 100)
    kopeiks = int(((x * 100 + y) * (1 + p / 100) + 10 ** -6) % 100)
    x = rubles
    y = kopeiks
    k -= 1

print(rubles, kopeiks)
