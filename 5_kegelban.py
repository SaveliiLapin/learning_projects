n, k = map(int, input().split())
balls = [1] * n

for i in range(k):
    l, r = map(int, input().split())

    for j in range(l - 1, r):
        balls[j] = 0

for i in balls:
    if i == 1:
        print('I', end='')
    else:
        print('.', end='')
