n = int(input())
x = float(input())
answ = 0.0

while n > 0:
    a = float(input())
    answ = (answ + a) * x
    n -= 1

a = float(input())
answ += a

print(answ)
