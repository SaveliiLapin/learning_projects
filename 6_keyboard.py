n = int(input())
c = list(map(int, input().split()))
k = int(input())
pj = list(map(int, input().split()))

for i in pj:
    c[i - 1] -= 1

for i in c:
    if i < 0:
        print('YES')
    else:
        print('NO')
