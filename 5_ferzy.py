x = []
y = []
is_beaten = False

for i in range(8):
    n, m = map(int, input().split())

    for j in range(len(x)):
        if n == x[j]:
            is_beaten = True
        elif m == y[j]:
            is_beaten = True
        elif abs(abs(x[j]) - abs(n)) == abs(abs(y[j]) - abs(m)):
            is_beaten = True

    x.append(n)
    y.append(m)

if is_beaten:
    print('YES')
else:
    print('NO')
